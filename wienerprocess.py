"""
wienerprocess.py

Simulates and optionally plots a normally distributed Wiener Process with
non-overlapping, independent periods
"""

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def wienerprocess(timesteps, paths, maturity, plot=False):
    """
    Parameters
    --------------
    timesteps (int) : number of timesteps until maturity
    paths (int) : number of paths to simulate
    maturity (double) : periods to which the simulation proceeds
    plot (boolean) : True to plot the simulation

    Returns
    ---------
    np.ndarray : timesteps+1 X paths Numpy array

    Usage
    -------
    W = wienerprocess(timesteps=100, paths=50, maturity=1.0, plot=True)
    """

    wienerpath = np.zeros((timesteps+1, paths), np.double)
    sqrt_time_step = math.sqrt(maturity / timesteps)

    normrand = sqrt_time_step * np.random.randn(timesteps, paths)

    for i in xrange(1, timesteps+1):
        wienerpath[i, :] = wienerpath[i-1, :] + normrand[i-1, :]

    if plot:
        plt.plot(wienerpath); plt.title('Wiener Process Plot'); plt.show();

    return wienerpath