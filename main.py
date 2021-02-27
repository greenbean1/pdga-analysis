"""
This is where the main magic happens and it all comes together
"""


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
        if opts.download.lower() not in [c.DL_OPTION_STATS, c.DL_OPTION_SEARCH]:
            print(f'Download option must be either "{c.DL_OPTION_STATS} or "{c.DL_OPTION_SEARCH}", not {opts.download}')
            return
    else:
        if opts.pdga_number is not None:
            print('Must include download option if specifying a PDGA number')
            return

    # Do stuff depending on which arguments the user passes
    if opts.download:
        download_type = opts.download.lower()
        if download_type == c.DL_OPTION_SEARCH:
            if opts.pdga_number is None:
                api_calls.get_mpo_us_player_data(api_call_player_search=True)
                csv_functions.make_fixed_player_info_csv(api_call_player_search=True)
            else:
                api_calls.get_player_data_via_pdga_number(opts.pdga_number, api_call_player_search=True)
        else:
            if opts.pdga_number is None:
                api_calls.get_mpo_us_player_data(api_call_player_search=False)
                csv_functions.make_fixed_player_info_csv(api_call_player_search=False)
            else:
                api_calls.get_player_data_via_pdga_number(opts.pdga_number, api_call_player_search=False)

    if opts.merge:
        df = dataframes.combine_dg_and_pop_data()
        df.to_csv(c.final_dataset_path, index=False)


if __name__ == '__main__':
    main()
