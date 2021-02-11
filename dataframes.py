"""
This module has the pandas related functions for data munging
"""

import os
import pandas as pd
from pathlib import Path


directory = os.getcwd()
filename = 'simple_file.csv'  # switch to player_search_data.csv
path_name = os.path.join(directory, filename)


def make_df():
    df_players = pd.read_csv(path_name)
    print(df_players.head())
