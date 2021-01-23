"""
This module has the PDGA API calls
"""

from http import HTTPStatus
import json
import requests
from typing import Dict, Tuple

API_LOGIN_URL = 'https://api.pdga.com/services/json/user/login'
PLAYER_STATS_URL = 'https://api.pdga.com/services/json/player-statistics?pdga_number=37817'


def _get_pdga_login() -> Dict[str, str]:
    print('Getting PDGA login info')
    with open('pdga_beau_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


def _get_new_pdga_session_info() -> Tuple[str, str]:
    print('Getting new PDGA API session info')
    request_login = requests.post(API_LOGIN_URL, data=_get_pdga_login())
    login_response = request_login.text  # Refactor here: requests_login.json
    login_response_dict = json.loads(login_response)
    print(login_response_dict)
    return login_response_dict["session_name"], login_response_dict["sessid"]


def _get_old_pdga_session_info() -> Dict[str, str]:
    print('Getting old PDGA API session info')
    with open('old_pdga_api_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'session_name': info[0], 'sessid': info[1]}

# Make me dumb! Take session_name & sessid and return JSON or fact that it failed (Throw my own error) - Try and Except in calling context
def get_player_info() -> Dict:
    try:
        old_session_info = _get_old_pdga_session_info()
        session_name, sessid = old_session_info['session_name'], old_session_info['sessid']
        player_info_eagle = requests.get(PLAYER_STATS_URL, cookies={session_name: sessid})
    session_name, sessid = _get_pdga_session_info()

    print(player_info_eagle)
    if player_info_eagle.status_code != HTTPStatus.OK:
        print(f'Failed to get player stats: status {player_info_eagle.status_code}')
        #  Add break/return
    else:  # Won't need else when in a function
        print('yay success getting player stats')
        player_info = player_info_eagle.json()
        print(f'Player info type = {type(player_info)}')
        print(player_info)
        print(player_info.get('players')[0])  # look into DotDict; lazy since could cause crash
    return {'test_key': 'test_value'}
