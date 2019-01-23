import numpy as np
from random import choices as chc

def mc_gen(self, *, n, datalength):
    '''
    feed dataset for bootstrapping draws, OR draws from param'd dist.
    '''
    results = chc(np.arange(0, datalength), k=n)
    return results
