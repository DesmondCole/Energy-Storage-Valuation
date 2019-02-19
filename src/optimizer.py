import numpy as np

def solve(R, P, q = 1):
    '''
    This runs a finite horizon backwards recursion to select the
    optimal state matrix and max value.
    R is an nd.array, of {sims, states, states, periods}
    P is an nd.array, of {sims, states, states, periods}
    q indicates the shortest possible switching time. Default to 1 hour.
    '''
    nsims, states, periods = R[:,:,0,:].shape
    optim_pol = np.zeros((nsims, periods))
    optim_val = np.zeros(nsims)
    for i in np.arange(0, nsims):
        V = np.zeros((states, periods))
        for j in np.arange(periods-2, -1, -1):
            for k in np.arange(0, states):
                V[k,j] = max(R[i,k,:,j] + np.multiply(P[i,k,:,j], V[:,j+1]))
            optim_pol[i,j] = np.argmax(V[:,j])
        optim_val[i] = max(V[:,j])
    results = {'opt_val': optim_val, 'opt_pol': optim_pol}
    return results
