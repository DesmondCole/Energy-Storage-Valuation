import pandas as pd
import numpy as np
from src import optimizer as opt
from src import generation

class DispatchAsset:
    '''
    Feeds the optimizer storage characteristics, and runs it to generate values.
    '''
    def __init__(self, *, asset, gen, market):
        reward_mat = self._rewardvals(asset=asset, market=market, gen=gen)
        prob_mat = self._probvals(asset=asset, gen=gen, market=market)
        results = opt.solve(reward_mat, prob_mat)
        self.testresults = {'reward':reward_mat, 'prob':prob_mat, 'vals':results}
        return None

    def _rewardvals(self, *, asset, market, gen):
        '''
        Incorporating the action and state spaces, as well as simulated
        prices and generation, develop a reward matrix that will be shipped
        to the optimizer for bellman equation optimization.

        Initially built with restriction that solar capacity equal storage cap.
        '''
        generation = gen['kw']
        prices = market['price']
        storage_capacity = asset['mw']

        states = np.arange(0, (storage_capacity+.1), .1)/storage_capacity
        periods = 24
        ancillary = .5
        rewardmat = np.zeros((len(states), len(states), periods))

        for i in np.arange(0,periods):
            solargen = generation[i]
            price = float(prices[i])
            rows = np.ones((1, len(states))).T
            solarmat = 1 - np.triu((rows * states) - (rows * states).T)
            solarrev = solarmat * solargen * price
            storagemat = 1 - solarmat.T
            storagerev = storagemat * storage_capacity * price + np.diag(ancillary * storage_capacity * states)
            rewardmat[:,:,i] = solarrev + storagerev
        return rewardmat

    def _probvals(self, *, asset, gen, market):
        '''
        generate transition probability matrix.
        '''
        generation = gen['kw']
        periods = 24
        states = np.arange(0, (asset['mw']+.1), .1)
        probmat = np.ones((len(states), len(states), periods))
        for i in np.arange(0,periods):
            maxstor = int(.001*generation[i])
            if maxstor<len(states):
                probmat[:(len(states) - maxstor), maxstor:, i] = np.tril(probmat[:(len(states) - maxstor), maxstor:, i])
        return probmat
