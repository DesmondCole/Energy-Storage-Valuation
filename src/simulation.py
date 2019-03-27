import pandas as pd
import numpy as np
from src import market as mkt

def simulate():
    """
    Govern overall simulation.
    """
    market = mkt.MarketSimulator(data = testdata)
    #add generation values
    #dispatch asset by calling the storage_opt file
    #iterate through time periods?
    return True
