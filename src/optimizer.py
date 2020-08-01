import numpy as np

def solve(R, P):
    '''
    R is a states X states X periods reward matrix
    P is a states X states X periods probability matrix
    '''
    states, periods = R[0,:,:].shape
    print('states: ', states)
    print('periods: ', periods)
    initialstate = int(states-1)
    optim_act = np.zeros((periods))
    Q = np.zeros((states, periods))
    for k in np.arange(0,states):
        Q[k, periods-1] = sum(np.multiply(P[k, :, periods-1], R[k, :, periods-1]))

    def bwsweep(period, state):
        for i in np.arange(periods-2, period, -1):
            for k in np.arange(0, states):
                Q[k, i] = sum(np.multiply(P[k, :, i], (R[k, :, i] + Q[:, i+1])))
        result = np.argmax(
            np.multiply(
            P[state, :, period],
            (R[state, :, period] + Q[:, (period+1)])
            )
        )

        print("optim_val: ", result, " at point: ", period)
        return result

    def fwsweep():
        optim_act[0] = int(bwsweep(0, initialstate))
        for i in np.arange(1, periods-1):
            optim_act[i] = int(bwsweep(i,int(optim_act[(i-1)])))
        return optim_act

    def calc_rev(policy):
        revenue = R[initialstate, int(policy[0]), 0]
        for i in np.arange(1,periods):
            revenue += R[int(policy[i-1]), int(policy[i]), i]
        return revenue

    optim_policy = fwsweep()
    revenue = 4*calc_rev(optim_policy)

    results = {'opt_act': optim_policy, 'revenue': revenue}

    return results
