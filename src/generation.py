import pandas as pd
import numpy as np

class Solar:
    '''
    simul: Obtain generation data using NREL's SAM.
    simple: Use actual generation data.
    '''
    def __init__(self, *, type):
        if type == 'simul':
            self.data = self._genvals()
        if type == 'simple':
            data = pd.read_csv('/Users/Desmond/Desktop/Work/Coding/GitHub/Storage/Energy-Storage-Valuation/data/generation.csv',
            parse_dates=['Time stamp'])
            data['date'] = data['Time stamp'].dt.date
            data['month'] = data['Time stamp'].dt.month
            data['year'] = data['Time stamp'].dt.year
            self.data = data.groupby(['Time stamp','month','year']).mean().reset_index()
            print("generation!:", self.data.dtypes)
        return None

    def _genvals(self):
        '''
        TBD: Add in SAM code.
        '''
        return True
