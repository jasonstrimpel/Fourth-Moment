"""

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

    Returns
    ---------

    Usage
    -------
    
    """
    W = wp.wienerprocess(timesteps, paths, maturity, plot=False)
    
    prices = s0 * math.exp((m - 0.5 * s) + (s * W))

    if plot:
        plt.plot(prices); plt.title('Evolved Stock Prices'); plt.show();