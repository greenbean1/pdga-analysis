"""
This module has CSV functions
"""

import csv
import os
from typing import Dict, List


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


def write_header(players: List[Dict[str, str]]) -> None:
    field_names = players[0].keys()
    with open(PLAYER_STATS_CSV, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)


# Write me please
def append_to_csv(players: List[Dict[str, str]]) -> None:
    with open(PLAYER_STATS_CSV, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for player in players:
            player_values = []
            for column_value in player.values():
                player_values.append(column_value)
            writer.writerow(player_values)
