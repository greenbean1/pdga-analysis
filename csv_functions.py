"""
This module has CSV functions
"""

import csv
import os
from typing import Dict


PLAYER_STATS_CSV = 'player_stats.csv'


def delete_player_stats_csv():
    try:
        os.remove(PLAYER_STATS_CSV)
        print('Successfully deleted player stats csv')
    except OSError:
        print('No player stats file to delete')


def dict_to_csv(player_dict: Dict[str, str]) -> None:
    field_names = player_dict.keys()
    with open(PLAYER_STATS_CSV, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)
        player_values = []
        for value in player_dict.values():
            player_values.append(value)
        writer.writerow(player_values)
