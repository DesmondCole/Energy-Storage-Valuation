import numpy as np

def solve(X, T, q = 1):
    '''
    This runs a markov decision model.
    X is an nd.array, of {nsims, states, hours}
    T is an nd.array, of {states, states}
    q indicates the shortest possible switching time. Default to 1 hour.
    '''
    for i in np.arange(0, nsims):
        U = X[i, :, :]
        V0 = np.zeros(states, hours)
        V1 = U[:, -1]
        for j in np.arange(hours - 1, 0, -1):
            for k in np.arange(0, states):
                V0[k, j] = arg.max(T[k, :] + V1)
            V1 = V0
