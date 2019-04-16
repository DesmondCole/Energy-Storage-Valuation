import pandas as pd
import numpy as np
from src import monte_carlo
from sklearn import linear_model as lm


class MarketSimulator:
    def __init__(self, *, testdata, method):
        if method == 'sim':
            runprices = self._calibration(data = testdata)
            self.results = runprices
        if method == 'mock':
            print('using mock prices')
            self.results = pd.read_csv('./data/mockprices.csv', parse_dates = ['timestamp'])
        return None

    def _do_prices(self, *, prices, sims):
        input_rels = self._calibration(data=prices)
        sim_inputs = monte_carlo.mc_gen(n=sims, datalength=len(prices))
        results = np.matmul(inputs=sim_inputs, coefs=input_rels)
        return results

    def _calibration(self, *, data):
        Y = data.iloc[:, 0]
        X = data.iloc[:, 1:]
        linmod = lm.LinearRegression().fit(X, Y)
        results = linmod.coef_
        return results
