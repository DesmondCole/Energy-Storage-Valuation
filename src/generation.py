import pandas as pd
import numpy as np

class Solar:
    '''
    simul: Obtain generation data using NREL's SAM.
    simple: Use actual generation data.
    '''
    def __call__(self, *, type):
        if type == 'simul':
            data = self._genvals(wx)
        if type == 'simple':
            data = pd.read_csv('../data/generation.csv', parse_dates=['LocalTime'])
            data['date'] = data['LocalTime'].dt.date
            data['month'] = data['date'].dt.month

    def _genvals(self, *, wx):
        '''
        Add in SAM code.
        '''
        return gen
