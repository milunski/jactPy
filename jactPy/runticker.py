"""
file executes the ticker
@author: matt milunski
"""

# import modules
import requests
import sys
import time
import subprocess
import pprint
from helperfuncs import tickerfunctions

# clear the screen
subprocess.call('clear')

# capture currency symbols from command line
refreshsec = tickerfunctions.check_refresh(int(sys.argv[1]))
currencies = tickerfunctions.check_currency(sys.argv[2:])
sort_currency = currencies.sort()

# instantiate pretty printing to shell
pp = pprint.PrettyPrinter(indent=2)

# keep an infinite loop going to constantly make api call to bittrex
while True:
    # use list as the data structure for storing ticker data and printing to cli
    output = list()
    
    # evaluate all ticker symbols and only retain data of those on bittrex
    for symbol in sort_currency:
        fetchdata = requests.get(
            f"https://api.bittrex.com/api/v1.1/public/getticker?market={symbol}"
        ).json()
        # TODO - add %change from lagged value
        if fetchdata['success'] is True:
            bid = fetchdata['result']['Bid']
            ask = fetchdata['result']['Ask']
            last = fetchdata['result']['Last']
            tick = str('Crypto: ' + symbol + 
            '    Price: ' + str(bid) + 
            '    Ask: ' + str(ask) + 
            '    Last: ' + str(last))
            output.append(tick)
    
    # all print stuff here... just trying to keep it somewhat pretty
    subprocess.call('clear')
    print(
        'Bittrex Cryptocurrency Exchange Ticker\nhttps://bittrex.com/home/markets'
    )
    pp.pprint(output)
    if refreshsec > 1:
        print(f'refreshing every {refreshsec} seconds...')
    else:
        print(f'refreshing every {refreshsec} second...')
        
    time.sleep(refreshsec)