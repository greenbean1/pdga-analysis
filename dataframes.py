"""
This module has the pandas related functions for data munging


Options:
Manual data removal/fixing
Use csv library to clean
"""

import numpy as np
import os
import pandas as pd

import constants as c


directory = os.getcwd()
filename = 'fixed_player_stats.csv'  # switch to player_search_data.csv
path_name = os.path.join(directory, filename)


def _clean_state_pop_data(df):
    df.columns = ['State', 'Population']
    for index, row in df.iterrows():
        df.at[index, 'State'] = row['State'][1:]
    return df


def load_state_pop_data():
    df_pop = pd.read_csv(c.STATE_POP_CSV, engine='python')
    clean_df_pop = _clean_state_pop_data(df_pop)
    print(clean_df_pop)
    return clean_df_pop


def _state_abbreviations_to_full(df):
    # Flip the dictionary in constants module to have keys be the abbreviations
    mapping = {value: key for key, value in c.STATE_ABBREVIATION_MAPPING.items()}
    df['state_prov'] = df['state_prov'].str.upper()
    for index, row in df.iterrows():
        if pd.notna(row['state_prov']):
            df.at[index, 'state_prov'] = mapping[row['state_prov']]
    return df


def _add_rating_flags(df):
    df['flag_950'] = np.where(df['rating'] >= 950, 1, 0)
    df['flag_1000'] = np.where(df['rating'] >= 1000, 1, 0)
    return df


def make_dg_summary_df():
    df_players = pd.read_csv(path_name, engine='python')
    df_players = _state_abbreviations_to_full(df_players)
    df_players = _add_rating_flags(df_players)
    df_agg = df_players.groupby('state_prov').agg(
        num_total_pros=('pdga_number', 'count'),
        num_950_pros=('flag_950', 'sum'),
        num_1000_pros=('flag_1000', 'sum')
    )
    df_agg = df_agg.reset_index()
    return df_agg


def combine_dg_and_pop_data():
    df_combined =
