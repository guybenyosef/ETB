import numpy as np

def poly_interpolation(X, Y):
    p = np.polyfit(X, Y, 5)
    h_step = 0.01
    ax = np.arange(X[3], X[4], h_step)
    ay = np.polyval(p, ax)
    return ax, ay