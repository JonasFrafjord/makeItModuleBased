# First, setup our environment

import numpy as np
import matplotlib.pyplot as plt
import time

from scipy.signal import sawtooth

T = 8 * np.pi
t = np.linspace(0, T, 512)
x = sawtooth(t)
plt.plot(t, x)

steps = 2048
mat = np.zeros((3,len(x)-2))
mat[0] = x[:-2]
mat[1] = x[1:-1]
mat[2] = x[2:]


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
def blur_py2(x, steps=1024):
    x = 1 * x # copy
    for _ in range(steps):
        x[1:-1] = .25*(mat[0]+2*mat[1]+mat[2])
        mat[0] = x[:-2]
        mat[1] = x[1:-1]
        mat[2] = x[2:]
    return x
def blur_py3(x, steps=1024):
    x = 1 * x # copy
    for _ in range(steps):
        x[1:-1] = .25*(x[:-2]+2*x[1:-1]+x[2:])
    return x

t0 = time.clock()
x_blurred = blur_py(x, steps)
t1 = time.clock()
x_blurred2 = blur_py2(x,steps)
t2 = time.clock()
x_blurred3 = blur_py3(x,steps)
t3 = time.clock()
diff1 = t1-t0
diff2 = t2-t1
diff3 = t3-t2
print(diff1,diff2,diff1/diff2)
print(diff2,diff3,diff2/diff3)
print(diff1,diff3,diff1/diff3)
plt.plot(t, x, '--')
plt.plot(t, x_blurred)
plt.plot(t, x_blurred2)
plt.plot(t, x_blurred3)




plt.show()
