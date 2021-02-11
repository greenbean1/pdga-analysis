"""
This is where the main magic happens and it all comes together
"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Option Parser (ex: command line option to just get data)

import api_calls
import dataframes
import os


if __name__ == '__main__':
    # api_calls.get_mpo_us_player_search_data()
    dataframes.make_df()
    # print(os.getcwd())
