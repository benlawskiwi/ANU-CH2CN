import numpy as np
import matplotlib.pyplot as plt

f, (ax1, ax2, ax3) = plt.subplots(3,1,sharex=True)

x,y = np.loadtxt('ANUscan.dat',delimiter=',',unpack=True)
Lx,Ly = np.loadtxt('Lykke.csv',unpack=True)
dx,dy = np.loadtxt('../Digitizer/DIB-8037.csv',delimiter=',',unpack=True)

EA = 12468
DIB = 12442.45365
#DIB=12459.5

dx *=0.1
dx = 1e7/dx

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
#ax = plt.subplot(3,1,2)
ax2.plot(x,y,label='ANU')
ax2.plot(Lx,Ly,'--',label='Lineberger')
ax2.plot((DIB,DIB),(0,b),'C6-.',label='DIB')
ax2.plot((EA,EA),(0,b),'C7-.',label='EA')
plt.legend()
#ax = plt.subplot(3,1,3)
ax3.plot(x,y,label='ANU')
ax3.plot(Lz,Ly,'C2--',label=r'Lineberger $-6.642$ cm$^{-1}$')
ax3.plot((DIB,DIB),(0,b),'C6-.',label='DIB')
ax3.plot((EA,EA),(0,b),'C7-.',label='EA')
plt.xlabel('Energy (cm$^{-1}$)')
plt.legend()
#ax = plt.subplot(3,2,1)
ax1.plot(dx,dy)
plt.show()
