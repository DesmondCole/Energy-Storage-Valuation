import pandas as pd
import numpy as np

class Solar:
    '''
    Simplified: use year's worth of actual data.
    Next: map from simulated weather to solar generation
    '''
    def __call__(self, *, type):
        if type == 'simul':
            #size = system_size
            #conv = efficiency
            '...'
            #gen = self._genvals(wx = wx, params = params)
        if type == 'simple':
            data = pd.read_csv('../data/generation.csv', parse_dates=['LocalTime'])
            data['date'] = data['LocalTime'].dt.date
            data['month'] = data['date'].dt.month

    def _genvals(self, *, wx, params):
        gen = np.matmul(wx, params)
        return gen
