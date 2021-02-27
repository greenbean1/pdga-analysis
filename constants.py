"""
This module has constants that the other modules use
"""


import os


directory = os.getcwd()

# Main
FINAL_DATASET_CSV = 'final_dataset.csv'
final_dataset_path = os.path.join(directory, FINAL_DATASET_CSV)
DL_OPTION_SEARCH = 'search'
DL_OPTION_STATS = 'stats'

# API Calls
PDGA_BEAU_INFO_FILE = 'pdga_beau_info.txt'
PDGA_SESSION_INFO_FILE = 'old_pdga_session_api_info.txt'
SESSION_NAME = 'session_name'
SESSION_ID = 'sessid'
API_URL_HEAD = 'https://api.pdga.com/services/json/'
API_LOGIN_URL = API_URL_HEAD + 'user/login'
PLAYER_SEARCH_URL = API_URL_HEAD + 'players?'
PLAYER_STATS_URL = API_URL_HEAD + 'player-statistics?'
EVENT_SEARCH_URL = API_URL_HEAD + 'event?'
COURSE_SEARCH_URL = API_URL_HEAD + 'course?'
# Query Options Here
PLAYER_SEARCH = 0
PLAYER_STATS = 1
EVENT_SEARCH = 2
COURSE_SEARCH = 3

# CSV Info
PLAYER_AGG_CSV_INITIAL = 'player_agg_info_initial.csv'
PLAYER_AGG_CSV_FIXED = 'player_agg_info_fixed.csv'
PLAYER_INDIVIDUAL_CSV = 'player_individual.csv'

# Dataframes
path_name_dg_csv = os.path.join(directory, PLAYER_AGG_CSV_FIXED)
STATE_POP_CSV = 'census_pop_data.csv'
# Column Names
# Columns used in final CSV
COL_STATE = 'State'
COL_POPULATION = 'Population'
COL_NUM_TOTAL_PROS = 'num_total_pros'
COL_NUM_950_PROS = 'num_950_pros'
COL_NUM_1000_PROS = 'num_1000_pros'
COL_DENSITY_TOTAL_PRO = 'density_total_pro'
COL_DENSITY_950 = 'density_950+'
COL_DENSITY_1000 = 'density_1000+'
# Columns used only in disc golf dataframe
COL_FLAG_950 = 'flag_950'
COL_FLAG_1000 = 'flag_1000'
COL_RATING = 'rating'
COL_PDGA_NUMBER = 'pdga_number'


# Sourced from: https://gist.github.com/rogerallen/1583593 &
# Enhanced from: http://app02.clerk.org/menu/ccis/Help/CCIS%20Codes/state_codes.html
STATE_ABBREVIATION_MAPPING = {
    'Armed Forces Europe': 'AE',
    'Armed Forces Pacific': 'AP',
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
