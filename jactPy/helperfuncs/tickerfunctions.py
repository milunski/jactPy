"""
command line function stuff
@author: matt milunski
"""

def check_refresh(input):
    if input >= 1:
        return input
    else:
        return 1
    
def check_currency(input):
    assert len(input) > 0, "you forgot to specify the crypto to track"
    return input