import numpy as np
from scipy.signal import sawtooth

def blur_py(x, steps=1024):
    x = 1 * x # copy
    y = np.empty_like(x)
    y[0] = x[0]
    y[-1] = x[-1]
    for _ in range(steps):
        for i in range(1, len(x)-1):
            y[i] = .25 * ( x[i-1] + 2 * x[i] + x[i+1] )
        x, y = y, x # swap for next step
    return x
def blur_pyV(x, steps=1024):
    x = 1 * x # copy
    for _ in range(steps):
        x[1:-1] = .25*(x[:-2]+2*x[1:-1]+x[2:])
    return x
