import numpy as np

def solve(X, T, q = 1):
    '''
    This runs a bellman.
    X is an nd.array, of {nsims, states, periods}
    T is an nd.array, of {states, states}
    q indicates the shortest possible switching time. Default to 1 hour.
    '''
    nsims, states, periods = X.shape
    optim_pol = np.zeros((nsims, periods))
    optim_val = np.zeros(nsims)
    for i in np.arange(0, nsims):
        U = X[i, :, :]
        V0 = np.zeros((states, periods))
        V1 = U[:, -1]
        for j in np.arange(periods-2, -1, -1):
            for k in np.arange(0, states):
                V0[k, j] = U[k, j] + max(T[:, k] + V1)
            V1 = V0[:, j]
        for j in np.arange(0, periods, 1):
            optim_pol[i, j] = np.argmax(V0[:, j])
        optim_val[i] = max(V1)
    results = dict()
    results["opt_val"] = optim_val
    results["opt_pol"] = optim_pol
    return results
