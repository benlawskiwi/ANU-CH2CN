import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ANUscan.dat',delimiter=',',unpack=True)
x1,y1 = np.loadtxt('threshold-off.dat',unpack=True)
x2,y2 = np.loadtxt('threshold-set.dat',unpack=True)
x = 1e7/x
y -= 100
y1 += 600
y2 += 1000

plt.plot(x,y,label='ANU')
plt.plot(x1,y1,label='Full Rot Model')
plt.plot(x2,y2,label='Detachment Threshold Set')
plt.legend()
plt.xlabel('energy (cm$^{-1}$)')
plt.yticks([])
plt.show()
