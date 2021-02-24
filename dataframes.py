"""
This module has the pandas related functions for data munging
"""

import numpy as np
import pandas as pd

import constants as c


def _clean_state_pop_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = ['State', 'Population']  # Make columns consistent across PDGA & Census Data
    for index, row in df.iterrows():
        df.at[index, 'State'] = row['State'][1:]  # Remove prepended period before two-letter state abbreviation
    return df


def load_state_pop_data() -> pd.DataFrame:
    df_pop = pd.read_csv(c.STATE_POP_CSV, engine='python')
    clean_df_pop = _clean_state_pop_data(df_pop)
    print(clean_df_pop)
    return clean_df_pop


def _state_abbreviations_to_full(df: pd.DataFrame) -> pd.DataFrame:
    # Flip the dictionary in constants module to have keys be the abbreviations
    mapping = {value: key for key, value in c.STATE_ABBREVIATION_MAPPING.items()}
    df['state_prov'] = df['state_prov'].str.upper()
    for index, row in df.iterrows():
        if pd.notna(row['state_prov']):
            df.at[index, 'state_prov'] = mapping[row['state_prov']]
    return df


def _add_rating_flags(df: pd.DataFrame) -> pd.DataFrame:
    df['flag_950'] = np.where(df['rating'] >= 950, 1, 0)
    df['flag_1000'] = np.where(df['rating'] >= 1000, 1, 0)
    return df


def make_dg_summary_df() -> pd.DataFrame:
    df_players = pd.read_csv(c.path_name_dg_csv, engine='python')
    df_players = _state_abbreviations_to_full(df_players)
    df_players = _add_rating_flags(df_players)
    df_agg = df_players.groupby('state_prov').agg(
        num_total_pros=('pdga_number', 'count'),
        num_950_pros=('flag_950', 'sum'),
        num_1000_pros=('flag_1000', 'sum')
    )
    df_agg = df_agg.reset_index()
    df_agg.rename(columns={'state_prov': 'State'}, inplace=True)
    return df_agg


def combine_dg_and_pop_data() -> pd.DataFrame:
    df_dg = make_dg_summary_df()
    df_pop = load_state_pop_data()
    df_combined = pd.merge(df_dg, df_pop, how='left', on='State')
    # print(df_combined.info())
    return df_combined


# Test to confirm does not need to return itself
def add_density_metrics(df: pd.DataFrame):
    df['density_total_pro'] = df['num_total_pros'] / df['Population']
    df['density_950+'] = df['num_950_pros'] / df['Population']
    df['density_1000+'] = df['num_1000+_pros'] / df['Population']
