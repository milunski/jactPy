# jactPy Documentation
`jactPy` is a fun little Python package for watching the Bittrex cryptocurrency exchange.  

As this is meant to be a command line program, it's nothing fancy. Simply specify the refresh interval (in seconds) and the crypto symbols and run it.  

This package was built using Python 3. **Python 2 is not supported**.  

## Running jactPy
1. From the terminal, navigate to the `jactPy` root directory.
2. Enter: `python3 runticker.py [refresh interval] [symbol1] [symbol2] [symbol...]`.
3. Enjoy! Use ctrl-C to kill the program.

## Example
Here's an example of using a 5 second refresh rate for Litecoin and Ethereum.  
`python3 runticker.py 5 BTC-LTC BTC-ETH`