import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ANUscan.dat',delimiter=',',unpack=True)
Lx,Ly = np.loadtxt('Lykke.csv',unpack=True)

EA = 12468
DIB = 12442.45365
#DIB=12459.5

x = 1e7/x
subr = np.logical_and(Lx>x[-1],Lx<x[0])
Lx = Lx[subr]
Ly = Ly[subr]

ofs = np.mean(Ly)-np.mean(y)
Ly -= ofs


#Calibration
subr = np.logical_and(x>12449,x<12465)
ay = y[subr]
ax = x[subr]
b = max(ay)
subi = np.logical_and(ay>b-0.001,ay<1000)
c = ax[subi]
print(b)
print(c)

subr = np.logical_and(Lx>12449,Lx<12465)
ay = Ly[subr]
ax = Lx[subr]
Lb = max(ay)
subi = np.logical_and(ay>Lb-0.001,ay<1000)
Lc = ax[subi]
print(Lb)
print(Lc)

ratio = b/Lb
Ly *= ratio
shift = Lc-c
#Lx -= shift
Lz = Lx-shift
print(shift)

#ofs = np.mean(Ly)-np.mean(y)
#Ly -= ofs
#Lx -= 5.5
ax = plt.subplot(2,1,1)
ax.plot(x,y,label='ANU')
ax.plot(Lx,Ly,'--',label='Lineberger')
ax.plot((DIB,DIB),(0,b),'C6-.',label='DIB')
ax.plot((EA,EA),(0,b),'C7-.',label='EA')
plt.legend()
ax = plt.subplot(2,1,2)
ax.plot(x,y,label='ANU')
ax.plot(Lz,Ly,'C2--',label=r'Lineberger $-6.642$ cm$^{-1}$')
ax.plot((DIB,DIB),(0,b),'C6-.',label='DIB')
ax.plot((EA,EA),(0,b),'C7-.',label='EA')
plt.xlabel('Energy (cm$^{-1}$)')
plt.legend()
plt.show()
