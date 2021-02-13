"""
This is where the main magic happens and it all comes together
"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Option Parser (ex: command line option to just get data)

import os
# import pandas as pd

import api_calls
import csv_functions
import dataframes

FINAL_DATASET_CSV = 'final_dataset.csv'
directory = os.getcwd()
final_dataset_path = os.path.join(directory, FINAL_DATASET_CSV)


if __name__ == '__main__':
    # api_calls.get_mpo_us_player_search_data()
    # header_names, correct_data = csv_functions.get_correct_data()
    # csv_functions.make_corrected_csv(header_names, correct_data)
    # dataframes.load_state_pop_data()
    df = dataframes.combine_dg_and_pop_data()
    # df = dataframes.add_density_metrics(df)
    df.to_csv(final_dataset_path, index=False)
