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


def find_messy_row_data() -> Dict[int, str]:
    messy_row_data_dict = {}
    correct_rows = ['first_name', 'last_name', 'pdga_number', 'membership_status', 'membership_expiration_date',
                    'classification']
    old_to_new_mappings = {'rating': 'city', 'rating_effective_date': 'state_prov', 'official_status': 'country',
                           'official_expiration_date': 'rating', 'last_modified': 'rating_effective_date'}
    with open(PLAYER_STATS_CSV, 'r', newline='') as csv_file_read:
        reader = csv.DictReader(csv_file_read)
        for i, row in enumerate(reader):
            if not row['official_status']:  # AKA if value in the official_status column is missing
                row_contents = []
                # First get columns that are correct_rows
                for correct_value in correct_rows:
                    row_contents.append(row[correct_value])
                # Then blank x3
                for j in range(3):
                    row_contents.append("")
                # Lastly rating = city, rating_effective_date =  state_prov, official_status = country, official_expiration_date = rating, last_modified = rating_effective_date
                messy_cols = old_to_new_mappings.keys()
                for cnt, messy_col in enumerate(messy_cols):
                    # row[messy_col] = row[old_to_new_mappings[messy_col]]
                    row_contents.append(row[old_to_new_mappings[messy_col]])  # Add to row the mapped correct values
                messy_row_data_dict[i] = row_contents
                # add logic to capture correct row data
    print(messy_row_data_dict)
    return messy_row_data_dict
    # with open(PLAYER_STATS_CSV, 'w', newline='') as csv_file_write:
    #     writer = csv.writer(csv_file_write)
    #     for i, row in enumerate(writer):
    #         if i in rows_to_clean:
    #             print('yay')

    #     csv_reader = csv.reader(csv_file)
    # with open(PLAYER_STATS_CSV, 'r', newline='') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     for row in csv_reader:
    #         if row.index_col(10) in (None, ""):
    #             print('hi')

    # if column 12 (official_status) is empty
        # append row number to rows_to_clean
        # Move column data over 3 columns
