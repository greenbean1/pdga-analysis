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


def _get_pdga_session_info() -> Tuple[str, str]:
    print('Getting PDGA sessid')
    request_login = requests.post(API_LOGIN_URL, data=_get_pdga_login())
    login_response = request_login.text  # Refactor here: requests_login.json
    login_response_dict = json.loads(login_response)
    print(login_response_dict)
    return login_response_dict["session_name"], login_response_dict["sessid"]


def get_player_info() -> Dict:
    pdga_session_info = _get_pdga_session_info()
    player_info_eagle = requests.get(PLAYER_STATS_URL, cookies={pdga_session_info[0]: pdga_session_info[1]})
    print(player_info_eagle)
    if player_info_eagle.status_code != HTTPStatus.OK:
        print(f'Failed to get player stats: status {player_info_eagle.status_code}')
        #  Add break/return
    else:  # Won't need else when in a function
        print('yay success getting player stats')
        player_info = player_info_eagle.json()
        print(player_info.get('players')[0])  # look into DotDict; lazy since could cause crash
    return {'test_key': 'test_value'}



    session_name, sessid = get_pdga_session_info()
    print(sessid)

