"""
This module has the PDGA API calls
"""


from http import HTTPStatus
import json
import requests
from typing import Dict, List, Tuple

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


# TODO Refactor below 4 functions to 2 with stats vs search as parameter & update constants module w/URLs
def get_player_stats_via_pdga_number(pdga_number: int) -> List[Dict[str, str]]:
    api_url = f'https://api.pdga.com/services/json/player-statistics?pdga_number={pdga_number}'
    try:
        print('Trying old PDGA session info')
        old_pdga_session_info = _get_old_pdga_session_info()
        return _get_player_info(api_url, old_pdga_session_info['session_name'], old_pdga_session_info['sessid'])
    except APICallFailed:  # Ask about correct way to do this!
        print('Trying new PDGA session info')
        new_pdga_session_info = _get_new_pdga_session_info()
        return _get_player_info(api_url, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])


def get_mpo_us_player_stats() -> None:
    limit = 200  # Varies between 10 and 200
    offset = 0  # 0+
    results_count = 0
    while True:
        try:
            # print('Trying old PDGA session info')
            old_pdga_session_info = _get_old_pdga_session_info()
            url_string = 'https://api.pdga.com/services/json/player-statistics?'
            url_string += f'division_code=MPO&country=US&year=2020&limit={limit}&offset={offset}'
            players_list = _get_player_info(url_string,
                                            old_pdga_session_info[c.SESSION_NAME],
                                            old_pdga_session_info[c.SESSION_ID])
            response_length = len(players_list)
            if offset == 0:
                csv_functions.write_header(players_list)
            csv_functions.append_to_csv(players_list)
            offset += limit
            results_count += response_length
            print(f'Cumulative players: {results_count}')
            if response_length != limit:
                print('Response length != limit')
                break
            if results_count > 200000:
                print('Results count > 200000')
                break
        except APICallFailed:  # Ask about correct way to do this!
            # Need to actually implement this
            print('Trying new PDGA session info')
            # new_pdga_session_info = _get_new_pdga_session_info()
            # return _get_player_info(url_string, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])
            break
    print(f'Total players returned: {results_count}')


def get_player_search_data_via_pdga_number(pdga_number: int) -> List[Dict[str, str]]:
    api_url = f'https://api.pdga.com/services/json/players?pdga_number={pdga_number}'
    try:
        print('Trying old PDGA session info')
        old_pdga_session_info = _get_old_pdga_session_info()
        return _get_player_info(api_url, old_pdga_session_info['session_name'], old_pdga_session_info['sessid'])
    except APICallFailed:  # Ask about correct way to do this!
        print('Trying new PDGA session info')
        new_pdga_session_info = _get_new_pdga_session_info()
        return _get_player_info(api_url, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])


def get_mpo_us_player_search_data() -> None:
    limit = 200  # Varies between 10 and 200
    offset = 0  # 0+
    results_count = 0
    while True:
        url = c.PLAYER_SEARCH_URL + f'class=P&country=US&limit={limit}&offset={offset}'
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
        # print(f'Response Length = {response_length}')
        if offset == 0:
            csv_functions.write_header(players_list)
        csv_functions.append_to_csv(players_list)
        offset += limit
        results_count += response_length
        print(f'Cumulative players: {results_count}')
        if response_length != limit:
            print('Response length != limit')
            break
        if results_count > 1000:
            print('Results count > 1000')
            break
    print(f'Total players returned: {results_count}')
