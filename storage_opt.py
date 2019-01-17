import pandas as pd
import numpy as np
import optimizer as opt

class DispatchAsset:
    '''
    Feeds the optimizer storage characteristics, and runs it to generate values.
    '''
    def __call__(self, *, asset, gen, market):
        opt_states = opt.solve(value_mat, trans_cost_mat)
        return opt_states
