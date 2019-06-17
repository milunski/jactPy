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

# instantiate pretty printing to shell
pp = pprint.PrettyPrinter(indent=2)

# make the api call to bittrex to return ticker data
while True:
    output = list()
    for symbol in currencies:
        fetchdata = requests.get(
            f"https://api.bittrex.com/api/v1.1/public/getticker?market={symbol}"
        ).json()
        if fetchdata['success'] is True:
            bid = fetchdata['result']['Bid']
            ask = fetchdata['result']['Ask']
            last = fetchdata['result']['Last']
            tick = str('Crypto: ' + symbol + 
            '    Bid: ' + str(bid) + 
            '    Ask: ' + str(ask) + 
            '    Last: ' + str(last))
        else:
            pass
        output.append(tick)
    subprocess.call('clear')
    print(
        'Bittrex Cryptocurrency Exchange Ticker\nAPI docs @ https://bittrex.github.io/api/v1-1'
    )
    pp.pprint(output)
    print(f'refreshing every {refreshsec} seconds...')
    time.sleep(refreshsec)