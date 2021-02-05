"""
This module has the PDGA API calls
"""

# TODO Pare down query to reduce result set... MPO US is over 200k (filter for only active/nonzero rating?)

from http import HTTPStatus
import json
import requests
from typing import Dict, List

import csv_functions

PDGA_BEAU_INFO_FILE = 'pdga_beau_info.txt'
PDGA_SESSION_INFO_FILE = 'old_pdga_session_api_info.txt'
API_LOGIN_URL = 'https://api.pdga.com/services/json/user/login'
SESSION_NAME = 'session_name'
SESSION_ID = 'sessid'


class SessionExpired(Exception):
    pass


def _get_pdga_login() -> Dict[str, str]:
    print('Getting PDGA login info')
    with open(PDGA_BEAU_INFO_FILE, 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


def _update_pdga_api_session_info_file(session_info: Dict[str, str]) -> None:
    print('Setting PDGA API session info')
    with open(PDGA_SESSION_INFO_FILE, 'w') as pc:
        pc.write(session_info[SESSION_NAME])
        pc.write('\n')
        pc.write(session_info[SESSION_ID])
        pc.write('\n')


#  Returns session_name and sessid of new PDGA API login
def _get_new_pdga_session_info() -> Dict[str, str]:
    print('Getting new PDGA API session info')
    request_login = requests.post(API_LOGIN_URL, data=_get_pdga_login())
    login_response = request_login.text  # Refactor here: requests_login.json
    login_response_dict = json.loads(login_response)
    print('API Login Response dictionary:')
    print(login_response_dict)
    _update_pdga_api_session_info_file(login_response_dict)
    return {SESSION_NAME: login_response_dict[SESSION_NAME], SESSION_ID: login_response_dict[SESSION_ID]}


def _get_old_pdga_session_info() -> Dict[str, str]:
    # print('Getting old PDGA API session info')
    with open(PDGA_SESSION_INFO_FILE, 'r') as pc:
        info = pc.read().splitlines()
    return {SESSION_NAME: info[0], SESSION_ID: info[1]}


def get_player_stats(url: str, session_name: str, sessid: str) -> List[Dict[str, str]]:
    # print('Getting player info')
    player_info = requests.get(url, cookies={session_name: sessid})
    if player_info.status_code != HTTPStatus.OK:
        print(f'Failed to get player stats: status {player_info.status_code}')
        raise SessionExpired('Failed to get player stats')
    else:
        # print('Got player info')
        print(player_info)
        return player_info.json().get('players')  # look into DotDict; lazy since could cause crash


def get_mpo_us_player_stats() -> None:
    limit = 200  # Varies between 10 and 200
    offset = 0  # 0+
    results_count = 0
    while True:  # while True -> in loop if get no data then break
        try:
            # print('Trying old PDGA session info')
            old_pdga_session_info = _get_old_pdga_session_info()
            url_string = 'https://api.pdga.com/services/json/player-statistics?'
            url_string += f'division_code=MPO&country=US&year=2020&limit={limit}&offset={offset}'
            players_list = get_player_stats(url_string,
                                            old_pdga_session_info[SESSION_NAME],
                                            old_pdga_session_info[SESSION_ID])
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
            if results_count > 200000:
                print('Results count > 200000')
                break
        except SessionExpired:  # Ask about correct way to do this!
            print('Trying new PDGA session info')
            break
            # Set txt file credentials!!
            # new_pdga_session_info = _get_new_pdga_session_info()
            # return get_player_stats(url_string, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])
    print(f'Total players returned: {results_count}')


def get_player_stats_via_pdga_number(pdga_number: int) -> Dict[str, str]:
    api_url = f'https://api.pdga.com/services/json/player-statistics?pdga_number={pdga_number}'
    try:
        print('Trying old PDGA session info')
        old_pdga_session_info = _get_old_pdga_session_info()
        return get_player_stats(api_url, old_pdga_session_info['session_name'], old_pdga_session_info['sessid'])
    except SessionExpired:  # Ask about correct way to do this!
        print('Trying new PDGA session info')
        new_pdga_session_info = _get_new_pdga_session_info()
        return get_player_stats(api_url, new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])
