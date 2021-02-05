"""
This is where the main magic happens and it all comes together
"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import api_calls

if __name__ == '__main__':
    api_calls.get_mpo_us_player_stats()  # player_info is a dictionary
    # print(api_calls.get_player_stats_via_pdga_number(38464))
