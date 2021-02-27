"""
This module has the pandas related functions for data munging
"""

# TODO constantize ALL column names

import numpy as np
import pandas as pd

import constants as c


def _clean_state_pop_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.COL_STATE, c.COL_POPULATION]  # Make columns consistent across PDGA & Census Data
    for index, row in df.iterrows():
        df.at[index, c.COL_STATE] = row[c.COL_STATE][1:]  # Remove prepended period before two-letter state abbreviation
    df[c.COL_POPULATION] = df[c.COL_POPULATION].str.replace(',', '').astype(int)
    return df


def load_state_pop_data() -> pd.DataFrame:
    df_pop = pd.read_csv(c.STATE_POP_CSV, engine='python')
    clean_df_pop = _clean_state_pop_data(df_pop)
    return clean_df_pop


def _state_abbreviations_to_full(df: pd.DataFrame) -> pd.DataFrame:
    # Flip the dictionary in constants module to have keys be the abbreviations
    mapping = {value: key for key, value in c.STATE_ABBREVIATION_MAPPING.items()}
    df.rename(columns={'state_prov': c.COL_STATE}, inplace=True)
    df[c.COL_STATE] = df[c.COL_STATE].str.upper()
    for index, row in df.iterrows():
        if pd.notna(row[c.COL_STATE]):
            df.at[index, c.COL_STATE] = mapping[row[c.COL_STATE]]
    return df


def _add_rating_flags(df: pd.DataFrame) -> pd.DataFrame:
    df[c.COL_FLAG_950] = np.where(df[c.COL_RATING] >= 950, 1, 0)
    df[c.COL_FLAG_1000] = np.where(df[c.COL_RATING] >= 1000, 1, 0)
    return df


def make_dg_summary_df() -> pd.DataFrame:
    df_players = pd.read_csv(c.path_name_dg_csv, engine='python')
    df_players = _state_abbreviations_to_full(df_players)
    df_players = _add_rating_flags(df_players)
    df_agg = df_players.groupby(c.COL_STATE).agg(  # Next time look into defining these column names via constants
        num_total_pros=(c.COL_PDGA_NUMBER, 'count'),
        num_950_pros=(c.COL_FLAG_950, 'sum'),
        num_1000_pros=(c.COL_FLAG_1000, 'sum')
    )
    df_agg = df_agg.reset_index()
    return df_agg


def combine_dg_and_pop_data() -> pd.DataFrame:
    df_dg = make_dg_summary_df()
    df_pop = load_state_pop_data()
    df_combined = pd.merge(df_pop, df_dg, how='inner', on=c.COL_STATE)
    df_combined = df_combined.dropna()
    df_combined[c.COL_DENSITY_TOTAL_PRO] = df_combined[c.COL_NUM_TOTAL_PROS] / df_combined[c.COL_POPULATION]
    df_combined[c.COL_DENSITY_950] = df_combined[c.COL_NUM_950_PROS] / df_combined[c.COL_POPULATION]
    df_combined[c.COL_DENSITY_1000] = df_combined[c.COL_NUM_1000_PROS] / df_combined[c.COL_POPULATION]
    return df_combined
