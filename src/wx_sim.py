import pandas as pd
import numpy as np
from src import monte_carlo

'''
Also needs to incorporate time period of simulation.
Need to consider whether to park date selection methods in here or in MC.
'''

def gen_sim(data, *, N):
    data = self._clean_wx_data(data)
    simindex = monte_carlo.mc_gen(N)

    return data

def _clean_wx_data()
