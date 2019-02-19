import pandas as pd
import numpy as np

class Solar:
    '''
    Simplified: use year's worth of actual data.
    Next: map from simulated weather to solar generation
    '''
    def __call__(self, *, system_size, efficiency, tilt, tracking, type):
        if type == 'simul':
            size = system_size
            conv = efficiency
            '...'
            gen = self._genvals(wx = wx, params = params)
        if type == 'simple':
            gen = pd.read_csv('../data/*.csv')[['Power(MW)']]

    def _genvals(self, *, wx, params):
        gen = np.matmul(wx, params)
        return gen
