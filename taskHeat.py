# First, setup our environment

from blurFun import *
import matplotlib.pyplot as plt
import time


T = 8 * np.pi
t = np.linspace(0, T, 512)
x = sawtooth(t)
plt.plot(t, x)

steps = 2048


t0 = time.clock()
x_blurred = blur_py(x, steps)
t1 = time.clock()
x_blurredV = blur_pyV(x,steps)
t2 = time.clock()
diff1 = t1-t0
diff2 = t2-t1
print(diff1,diff2,diff1/diff2)
plt.plot(t, x, '--')
plt.plot(t, x_blurred)
plt.plot(t, x_blurredV)




plt.show()
