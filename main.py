"""
This is where the main magic happens and it all comes together
"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import api_calls
import csv_functions

if __name__ == '__main__':
    player_info = api_calls.get_eagle_stats()  # player_info is a dictionary
    # print(type(player_info))
    # print(player_info)
    csv_functions.dict_to_csv(player_info)
