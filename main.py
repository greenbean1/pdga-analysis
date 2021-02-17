"""
This is where the main magic happens and it all comes together
"""


import api_calls
import constants as c
import csv_functions
import dataframes


if __name__ == '__main__':
    # if option = save then save if analyse then analyze -> Implement via PyCharm configurations
    # if option = get data
        # api_calls.get_mpo_us_player_search_data()
    # elif option = clean data
        # header_names, correct_data = csv_functions.get_correct_data()
        # csv_functions.make_corrected_csv(header_names, correct_data)
    # dataframes.load_state_pop_data()
    df = dataframes.combine_dg_and_pop_data()
    # df = dataframes.add_density_metrics(df)
    df.to_csv(c.final_dataset_path, index=False)
