# Pull down JSON of 1 player statistics via Requests library
# Use Requests library + Postman to pull player stats - https://requests.readthedocs.io/en/master/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from http import HTTPStatus
import json
import requests
from typing import Dict, Tuple

PDGA_API_LOGIN_URL = 'https://api.pdga.com/services/json/user/login'


def get_pdga_login() -> Dict[str, str]:
    print('Getting PDGA login info')
    with open('pdga_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


def get_pdga_session_info() -> Tuple[str, str]:
    print('Getting PDGA sessid')
    request_login = requests.post(PDGA_API_LOGIN_URL, data=get_pdga_login())
    login_response = request_login.text  # Refactor here: requests_login.json
    login_response_dict = json.loads(login_response)
    print(login_response_dict)
    return login_response_dict["session_name"], login_response_dict["sessid"]


if __name__ == '__main__':
    session_name, sessid = get_pdga_session_info()
    print(sessid)
    url = 'https://api.pdga.com/services/json/player-statistics?pdga_number=37817'
    player_info_eagle = requests.get(url, cookies={session_name: sessid})
    print(player_info_eagle)
    if player_info_eagle.status_code != HTTPStatus.OK:
        print(f'Failed to get player stats: status {player_info_eagle.status_code}')
        #  Add break/return
    else:  # Won't need else when in a function
        print('yay success getting player stats')
        player_info = player_info_eagle.json()
        print(player_info.get('players')[0])  # look into DotDict; lazy since could cause crash


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
