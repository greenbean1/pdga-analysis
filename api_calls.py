"""
This module has the PDGA API calls
"""


from http import HTTPStatus
import json
import requests
from typing import Dict, List

import constants as c
import csv_functions


class APICallFailed(Exception):
    pass


def _get_pdga_login() -> Dict[str, str]:
    print('Getting PDGA login info')
    with open(c.PDGA_BEAU_INFO_FILE, 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


def _update_pdga_api_session_info_file(session_info: Dict[str, str]) -> None:
    print('Setting PDGA API session info')
    with open(c.PDGA_SESSION_INFO_FILE, 'w') as pc:
        pc.write(f'{session_info[c.SESSION_NAME]}\n')
        pc.write(f'{session_info[c.SESSION_ID]}\n')


#  Returns session_name and sessid of new PDGA API login
def _get_new_pdga_session_info() -> Dict[str, str]:
    print('Getting new PDGA API session info')
    request_login = requests.post(c.API_LOGIN_URL, data=_get_pdga_login())
    # If needed to be robust, would add status code checking to POST
    login_response = request_login.text  # Could refactor here: requests_login.json and remove json import statement
    login_response_dict = json.loads(login_response)
    print('API Login Response dictionary:', login_response_dict)
    _update_pdga_api_session_info_file(login_response_dict)
    return {c.SESSION_NAME: login_response_dict[c.SESSION_NAME], c.SESSION_ID: login_response_dict[c.SESSION_ID]}


def _get_old_pdga_session_info() -> Dict[str, str]:
    print('Getting old PDGA API session info')
    with open(c.PDGA_SESSION_INFO_FILE, 'r') as pc:
        info = pc.read().splitlines()
    return {c.SESSION_NAME: info[0], c.SESSION_ID: info[1]}


def _get_player_info(url: str, session_name: str, sessid: str) -> List[Dict[str, str]]:
    print('Getting player info')
    player_info = requests.get(url, cookies={session_name: sessid})
    if player_info.status_code != HTTPStatus.OK:
        raise APICallFailed(f'Failed to get player stats {player_info.status_code}')
    else:
        player_info = player_info.json().get('players')
        print('Got player info:', player_info)
        return player_info  # look into DotDict; lazy since could cause crash


def get_player_data_via_pdga_number(pdga_number: int, api_call_player_search: bool = True) -> None:
    if api_call_player_search:
        url = c.PLAYER_SEARCH_URL + f'pdga_number={pdga_number}'
    else:
        url = c.PLAYER_STATS_URL + f'pdga_number={pdga_number}'
    try:
        print('Trying old PDGA session info')
        old_pdga_session_info = _get_old_pdga_session_info()
        player_entry = _get_player_info(url, old_pdga_session_info['session_name'], old_pdga_session_info['sessid'])
        csv_functions.write_header(player_entry, individual=True)
        csv_functions.append_to_csv(player_entry, individual=True)
    except APICallFailed:
        print('Trying new PDGA session info')
        new_pdga_session_info = _get_new_pdga_session_info()
        player_entry = _get_player_info(url, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])
        csv_functions.write_header(player_entry, individual=True)
        csv_functions.append_to_csv(player_entry, individual=True)


def get_mpo_us_player_data(api_call_player_search: bool = True) -> None:
    limit = 200  # Varies between 10 and 200
    offset = 0  # 0+
    results_count = 0
    max_results = 9999  # Failsafe to ensure while loop breaks at some point
    while True:
        if api_call_player_search:
            url = c.PLAYER_SEARCH_URL + f'class=P&country=US&limit={limit}&offset={offset}'
        else:
            url = c.PLAYER_STATS_URL + f'division_code=MPO&country=US&year=2020&limit={limit}&offset={offset}'
        try:  # Try / Except to handle old vs new PDGA session info
            print('Trying old PDGA session info')
            old_pdga_session_info = _get_old_pdga_session_info()
            players_list = _get_player_info(url,
                                            old_pdga_session_info[c.SESSION_NAME],
                                            old_pdga_session_info[c.SESSION_ID])
        except APICallFailed:
            try:
                print('Trying new PDGA session info')
                new_pdga_session_info = _get_new_pdga_session_info()
                players_list = _get_player_info(url,
                                                new_pdga_session_info[c.SESSION_NAME],
                                                new_pdga_session_info[c.SESSION_ID])
            except APICallFailed:  # API call failed with new PDGA session info
                print('New PDGA session info failed')
                return
        response_length = len(players_list)
        if offset == 0:
            csv_functions.write_header(players_list, individual=False)
        csv_functions.append_to_csv(players_list, individual=False)
        offset += limit
        results_count += response_length
        print(f'Cumulative players: {results_count}')
        if response_length != limit:
            print('Response length != limit')
            break
        if results_count > max_results:  # Protective measure to ensure while loop breaks
            print(f'Reached failsafe limit - results count > {max_results}')
            break
    print(f'Total players returned: {results_count}')
