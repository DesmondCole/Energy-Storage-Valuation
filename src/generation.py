import pandas as pd
import numpy as np
from src import PySSC

class Solar:
    '''
    simul: Obtain generation data using NREL's SAM.
    simple: Use actual generation data.
    '''
    def __init__(self, *, type):
        if type == 'simul':
            self.data = self._genvals()
        if type == 'simple':
            data = pd.read_csv('../data/generation.csv', parse_dates=['Time stamp'])
            data['date'] = data['Time stamp'].dt.date
            data['month'] = data['Time stamp'].dt.month
            self.data = data.groupby(['Time stamp','month','year']).mean().reset_index()
        return None

    def _genvals(self):
        '''
        Add in SAM code.
        '''



        return True
