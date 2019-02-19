import pandas as pd
import numpy as np
from src import optimizer as opt
from src import generation

class DispatchAsset:
    '''
    Feeds the optimizer storage characteristics, and runs it to generate values.
    '''
    def __call__(self, *, asset, gen, market):
        opt_states = opt.solve(value_mat, trans_cost_mat)
        gen = gen
        '''
        work here to define rewards and transition values
        '''
        return opt_states
