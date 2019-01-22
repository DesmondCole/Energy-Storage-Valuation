import pandas as pd
import numpy as np
import sklearn as skl

class MarketSimulator:
    def __init__(self, *, prices):
        sim_prices = self._do_prices(prices = prices, sims = nsims)
        return sim_prices

    def _do_prices(self, *, prices, sims):
        input_rels = self._calibration(data = prices)
        sim_inputs = self._montecarlo(n = sims)
        results = np.matmul(inputs = sim_inputs, coefs = input_rels)
        return results

    def _calibration(self, *, data):
        Y = data[, 0]
        X = data[, 1:]
        linmod = skl.LassoCV(Y, X)
        results = linmod.coef_
        return results
