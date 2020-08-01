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
    market = mkt.MarketSimulator(method = 'mock')

    testbattery = stgchr.Asset(
        dod = .86
        , mw_cap = 1
        , roundtrip = .9
        , mwh_cap = 60
        , degrad = .99
    ).traits

    generation = gntn.Solar(type = 'simple')


    #loop across year and month
    for i in market.results['year'].unique():
        print('year: ', i)
        for j in market.results['month'].unique():
            print('month: ', j)
            test = stgopt.DispatchAsset(
            asset=testbattery
            , gen=generation.data[(generation.data['year'] == i) & (generation.data['month'] == j)]
            , market=market.results[(market.results['year'] == i) & (market.results['month'] == j)]
            )

    return test.testresults
