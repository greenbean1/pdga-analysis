"""
This module has constants that the other modules use
"""


import os


directory = os.getcwd()

# Main
FINAL_DATASET_CSV = 'final_dataset.csv'
final_dataset_path = os.path.join(directory, FINAL_DATASET_CSV)

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

# CSV
PLAYER_STATS_CSV = 'player_stats.csv'
FIXED_PLAYER_STATS_CSV = 'fixed_player_stats.csv'

# Dataframes
FINAL_DG_CSV = 'fixed_player_stats.csv'
path_name_dg_csv = os.path.join(directory, FINAL_DG_CSV)
STATE_POP_CSV = 'census_pop_data.csv'
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
