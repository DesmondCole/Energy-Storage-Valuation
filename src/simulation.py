import pandas as pd
import numpy as np
import datetime as dt
from src import market as mkt
from src import storage_char as stgchr
from src import storage_opt as stgopt
from src import generation as gntn

def simulate():
    """
    Govern overall simulation.
    """
    market = mkt.MarketSimulator(data = testdata, method = 'mock')
    testbattery = sc.Asset(
        dod = .86
        , mw_cap = 15
        , roundtrip = .9
        , mwh_cap = 60
        , degrad = .99)
    generation = gntn.Solar(type = 'simple')

    #loop across year and month
    for i in market.results['year'].unique():
        for j in market.results['month'].unique():
            stgopt.DispatchAsset(asset = testbattery,
            gen = generation.results[(generation.results['year'] == i) & (generation.results['month'] == j)],
            market = market.results[(market.results['year'] == i) & (market.results['month'] == j)])
    return True
