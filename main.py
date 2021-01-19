# Pull down JSON of 1 player statistics via Requests library
# Use Requests library + Postman to pull player stats - https://requests.readthedocs.io/en/master/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json

PDGA_API_LOGIN_URL = 'https://api.pdga.com/services/json/user/login'


def get_pdga_login():  # -> Dict[str, str]:
    print('Getting PDGA login info')
    with open('pdga_info.txt', 'r') as pc:
        info = pc.read().splitlines()
    return {'username': info[0], 'password': info[1]}


def get_pdga_sessid() -> str:
    print('Getting PDGA sessid')
    request_login = requests.post(PDGA_API_LOGIN_URL, data=get_pdga_login())
    login_response = request_login.text
    login_response_dict = json.loads(login_response)
    return login_response_dict["sessid"]


if __name__ == '__main__':
    sessid = get_pdga_sessid()
    print(sessid)
    url = 'https://api.pdga.com/services/json/player-statistics?pdga_number=37817'
    # cookie = dict(session_name='iM-aNzJdNUFXrOVdL_H4pstXiViIA9MqyBMMBcVbmxY')
    cookies = dict(session_name=sessid)
    print(cookie)
    player_info_eagle = requests.get(url, cookies=cookies)
    print(player_info_eagle)
    print(player_info_eagle.content)
    print(player_info_eagle.text)
    print(player_info_eagle.json)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
