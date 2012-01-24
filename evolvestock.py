"""
evolvestock.py

Simulates and optionally plots a stock process with non-overlapping,
independent periods
"""

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import wienerprocess as wp

def evolvestock(s0, m, s, timesteps, paths, maturity, plot=False):
    """
    Parameters
    --------------
    s0 (double) : initial stock proce
    m (double) : drift
    s (double) : volatility
    timesteps (int) : number of timesteps until maturity
    paths (int) : number of paths to simulate
    maturity (double) : periods to which the simulation proceeds
    plot (boolean) : True to plot the simulation
    
    Returns
    ---------
    np.ndarray : timesteps+1 X paths Numpy array
    
    Usage
    -------
    S = evolvestock(50, 0.05, 0.20, 100, 50, 1.0, plot=True)
    """
    W = wp.wienerprocess(timesteps, paths, maturity, plot=False)
    
    prices = s0 * np.exp((m - 0.5 * s) + (s * W))

    if plot:
        plt.plot(prices); plt.title('Evolved Stock Prices'); plt.show();
    
    return prices