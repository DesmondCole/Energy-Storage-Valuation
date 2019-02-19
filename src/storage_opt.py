import pandas as pd
import numpy as np
from src import optimizer as opt
from src import generation

class DispatchAsset:
    '''
    Feeds the optimizer storage characteristics, and runs it to generate values.
    '''
    def __call__(self, *, asset, gen, market):
        reward_mat = self._rewardvals(asset = asset)
        prob_mat = self._probvals(asset = asset, gen = gen, market = market)
        opt_states = opt.solve(reward_mat, prob_mat)
        return opt_states

    def _rewardvals(self, *, asset, market):
        '''
        use transition profile to generate reward matrix.
        market is a dictionary of prices, sims, and generation.
        '''
        periods = 24
        sims = market['sims']
        prices = market['prices']
        rawmat = np.zeros((sims, asset['mw_cap'], asset['mw_cap'], periods))
        for i in np.arange(0, sims):
            for j in np.arange(0, periods):
                rawmat[i, :, :, j] = np.matrix([[0,0,0],[.5,0,0],[1,.5,0]])
                rawmat[i, :, :, j] = np.tril(rawmat[i, :, :, j])
                rawmat[i, :, :, j] = prices[i, j] * rawmat[i, :, :, j]
        results = rawmat
        return results

    def _probvals(self, *, asset, gen, market):
        '''
        use asset, generation, and market characteristics to generate transition
        probability matrix.
        '''
        periods = 24
        sims = gen['sims']
        results = np.zeros((sims, asset['mw_cap'], asset['mw_cap'], periods))
        generation = gen['generation']
        rawmat = np.zeros((sims, asset['mw_cap'], asset['mw_cap'], periods))
        for i in np.arange(0, sims):
            for j in np.arange(0, periods):
                rawmat[i, :, :, j] = np.matrix([[0,0,0],[.5,0,0],[1,.5,0]])
                rawmat[i, :, :, j] = np.tril(rawmat[i, :, :, j])
                rawmat[i, :, :, j] = prices[i, j] * rawmat[i, :, :, j]
        results = rawmat
        return results
