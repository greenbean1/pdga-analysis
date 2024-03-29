"""
This module has functions relating to CSV files
"""

import csv
from shutil import copy
from typing import Any, Dict, List, Tuple

import constants as c


def write_header(players: List[Dict[str, str]], individual: bool) -> None:
    field_names = players[0].keys()
    if individual:
        filename = c.PLAYER_INDIVIDUAL_CSV
    else:
        filename = c.PLAYER_AGG_CSV_INITIAL
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)


def append_to_csv(players: List[Dict[str, str]], individual: bool) -> None:
    if individual:
        filename = c.PLAYER_INDIVIDUAL_CSV
    else:
        filename = c.PLAYER_AGG_CSV_INITIAL
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for player in players:
            player_values = []
            for column_value in player.values():
                player_values.append(column_value)
            writer.writerow(player_values)


def _get_correct_data() -> Tuple[List[str], Dict[int, List[Any]]]:
    fixed_data_dict = {}
    correct_rows = ['first_name', 'last_name', 'pdga_number', 'membership_status', 'membership_expiration_date',
                    'classification']
    old_to_new_mappings = {'rating': 'city', 'rating_effective_date': 'state_prov', 'official_status': 'country',
                           'official_expiration_date': 'rating', 'last_modified': 'rating_effective_date'}
    with open(c.PLAYER_AGG_CSV_INITIAL, 'r', newline='') as csv_file_read:
        reader = csv.DictReader(csv_file_read)
        for i, row in enumerate(reader):
            if i == 0:
                header_names = list(row.keys())
            row_contents = []
            if not row['official_status']:  # AKA if value in the official_status column is missing
                # First get columns that are correct_rows
                for correct_value in correct_rows:
                    row_contents.append(row[correct_value])
                # Then blank x3
                for j in range(3):
                    row_contents.append("")
                # Lastly map old columns to new correct column values as shown above in dictionary
                messy_cols = old_to_new_mappings.keys()
                for messy_col in messy_cols:
                    row_contents.append(row[old_to_new_mappings[messy_col]])  # Add to row the mapped correct values
            else:  # AKA if the data in that row is already correct
                for correct_value in row:
                    row_contents.append(row[correct_value])
            fixed_data_dict[i] = row_contents
    return header_names, fixed_data_dict


def make_fixed_player_info_csv(api_call_player_search: bool = True) -> None:
    if api_call_player_search:
        header_names, correct_data = _get_correct_data()
        with open(c.PLAYER_AGG_CSV_FIXED, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header_names)
            for correct_row in correct_data.values():
                writer.writerow(correct_row)
    else:
        print('Copying player stats csv')
        copy(c.PLAYER_AGG_CSV_INITIAL, c.PLAYER_AGG_CSV_FIXED)
