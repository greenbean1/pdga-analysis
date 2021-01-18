# Pull down JSON of 1 player statistics via Requests library
# Use Requests library + Postman to pull player stats - https://requests.readthedocs.io/en/master/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


r = requests.get('https://api.github.com/events')

#POST request w/URL & Body (contains username & password)
#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(r)
    print('heyy')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
