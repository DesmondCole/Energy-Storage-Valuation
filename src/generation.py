import pandas as pd
import numpy as np

class Solar:
    '''
    Map from simulated weather to solar generation
    '''
    def __init__(self, *, system_size, efficiency, tilt, tracking):
        size = system_size
        conv = efficiency

    def genvals(self, *, wx, size, conv):
        gen = np.matmul(wx, params)
        return gen
