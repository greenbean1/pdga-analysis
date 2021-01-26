"""
This module has the PDGA API calls
"""

from http import HTTPStatus
import json
import requests
from typing import Dict

API_LOGIN_URL = 'https://api.pdga.com/services/json/user/login'
PLAYER_STATS_URL = 'https://api.pdga.com/services/json/player-statistics?pdga_number=37817'


def _get_pdga_login() -> Dict[str, str]:
    print('Getting PDGA login info')
    with open('pdga_beau_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


# Haven't actually tested this
def update_pdga_api_session_info_file(session_info: Dict[str, str]) -> None:
    print('Setting PDGA API session info')
    with open('old_pdga_api_info.txt', 'w') as pc:
        pc.truncate()
        pc.write(session_info['session_name'])
        pc.write('\n')
        pc.write(session_info['sessid'])


#  Returns session_name and sessid of new PDGA API login
def _get_new_pdga_session_info() -> Dict[str, str]:
    print('Getting new PDGA API session info')
    request_login = requests.post(API_LOGIN_URL, data=_get_pdga_login())
    login_response = request_login.text  # Refactor here: requests_login.json
    login_response_dict = json.loads(login_response)
    print('API Login Response dictionary:')
    print(login_response_dict)
    update_pdga_api_session_info_file(login_response_dict)
    return {'session_name': login_response_dict['session_name'], 'sessid': login_response_dict['sessid']}


def _get_old_pdga_session_info() -> Dict[str, str]:
    print('Getting old PDGA API session info')
    with open('old_pdga_api_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'session_name': info[0], 'sessid': info[1]}


def get_player_stats(session_name: str, sessid: str) -> Dict[str, str]:
    print('Getting player info')
    player_info_eagle = requests.get(PLAYER_STATS_URL, cookies={session_name: sessid})
    if player_info_eagle.status_code != HTTPStatus.OK:
        print(f'Failed to get player stats: status {player_info_eagle.status_code}')
        raise Exception('Failed to get player stats')
    else:
        print('Got player info Eagle')
        print(player_info_eagle)
        return player_info_eagle.json().get('players')[0]  # look into DotDict; lazy since could cause crash


def get_eagle_stats() -> Dict[str, str]:
    try:
        print('Trying old PDGA session info')
        old_pdga_session_info = _get_old_pdga_session_info()
        return get_player_stats(old_pdga_session_info['session_name'], old_pdga_session_info['sessid'])
    except Exception:  # Ask about correct way to do this!
        print('Trying new PDGA session info')
        # Set txt file credentials!!
        new_pdga_session_info = _get_new_pdga_session_info()
        return get_player_stats(new_pdga_session_info['session_name'], new_pdga_session_info['sessid'])
