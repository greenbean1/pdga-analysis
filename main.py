"""
This is where the main magic happens and it all comes together
"""
# TODO Get command line options working


import argparse

import api_calls
import constants as c
import csv_functions
import dataframes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download', type=str, help='Download PDGA data')
    parser.add_argument('-p', '--pdga_number', type=int, help='Optional: specify PDGA number for downloading data')
    parser.add_argument('-m', '--merge', action='store_true', help='Merge PDGA data with population data')
    opts = parser.parse_args()

    # Ensure user arguments are valid
    if opts.download:  # if download has a value, must be either stats or search
        if opts.download.lower() not in ['stats', 'search']:
            print(f'Download option must be either "stats" or "search", not {opts.download}')
            return
    else:
        if opts.pdga_number is not None:
            print('Must include download option if specifying a PDGA number')
            return

    if opts.download:
        download_type = opts.download.lower()
        if download_type == 'search':
            if opts.pdga_number is None:
                api_calls.get_mpo_us_player_data()
            else:
                api_calls.get_player_data_via_pdga_number(opts.pdga_number)
            csv_functions.make_corrected_csv()
        else:
            if opts.pdga_number is None:
                api_calls.get_mpo_us_player_data(False)
            else:
                api_calls.get_player_data_via_pdga_number(opts.pdga_number, False)

    if opts.merge:
        df = dataframes.combine_dg_and_pop_data()
        df.to_csv(c.final_dataset_path, index=False)

    # Download PDGA player data to CSV (player stats or player search & by PDGA number (1) or en masse)
    # -> Include CSV data cleaning
    # Merge PDGA player data with Population Data to produce a CSV

    # if option = save then save if analyse then analyze -> Implement via PyCharm configurations
    # if option = get data
        # api_calls.get_mpo_us_player_search_data()
    # elif option = clean data
        # csv_functions.make_corrected_csv()
    # dataframes.load_state_pop_data()


if __name__ == '__main__':
    main()
