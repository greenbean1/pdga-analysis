"""
This module has the pandas related functions for data munging


Options:
Manual data removal/fixing
Use csv library to clean
"""

import os
import pandas as pd
from pathlib import Path


directory = os.getcwd()
filename = 'fixed_player_stats.csv'  # switch to player_search_data.csv
path_name = os.path.join(directory, filename)


def make_df():
    df_players = pd.read_csv(path_name, engine='python')
    print(df_players)
