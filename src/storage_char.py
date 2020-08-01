import pandas as pd
import numpy as np

class Asset:
    '''
    Allows for definition of characteristics
    '''
    def __init__(self, *, dod, mw_cap, mwh_cap, roundtrip, degrad):
        '''
        here should go mappings from raw characteristics to functions that are \
        relevant to calculating value.
        '''
        self.traits = {
        'mw':mw_cap
        , 'mwh':mwh_cap
        , 'roundtrip':roundtrip
        , 'degrad':degrad
        , 'dod':dod
        }
