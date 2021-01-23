"""
This is where the main magic happens and it all comes together
"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import api_calls

if __name__ == '__main__':
    player_info = api_calls.get_player_info()
    print(player_info)
