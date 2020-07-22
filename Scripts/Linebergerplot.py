import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ANUscan.dat',delimiter=',',unpack=True)
Lx,Ly = np.loadtxt('Lykke.csv',unpack=True)
dx,dy = np.loadtxt('../Digitizer/DIB-8037.csv',delimiter=',',unpack=True)
sx,sy = np.loadtxt('../Digitizer/sar07b.csv',delimiter=',',unpack=True)
sx2,sy2 = np.loadtxt('../Digitizer/sar07c2.csv',delimiter=',',unpack=True)
mx,my = np.loadtxt('../Digitizer/mabs17a.csv',delimiter=',',unpack=True)
spec = np.loadtxt('0wavenumber10K.txt', usecols=(0, 1, 2), unpack=True)

#Mabbs17 Model
mx = spec[0]+12468
my = spec[2]

#Mabbs17 Data
v = (max(my)-min(my))/(max(y)-min(y))
my /=v
my -= 600


#Sarre07 Rotational Model
sx *=0.1
sx = 1e7/sx
v = (max(sy)-min(sy))/(max(y)-min(y))
sy /=v
v = np.mean(sy)
sy +=1200-v
#Sarre07 at 2.7K
sx2 *=0.1
sx2 = 1e7/sx2
v = (max(sy2)-min(sy2))/(max(y)-min(y))
sy2 /=v
v = np.mean(sy2)
sy2 +=1300-v

#DIB Astro
dx *=0.1
dx = 1e7/dx
v = (max(dy)-min(dy))/(max(y)-min(y))
dy /=v
v = np.mean(dy)
dy +=2000-v
#ANU
x = 1e7/x
#Lineberger
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

#Plotting Shifts
#Ly +=600

#plt.plot(x,y,label='ANU')
plt.plot(Lx,Ly,'C1',label='Lineberger87')
plt.plot(dx,dy,'C2',label='Astro - DIB')
plt.plot(sx,sy,'C3',label='Sarre07 Model')
plt.plot(sx2,sy2,'C4',label='Sarre07 2.7K')
#plt.plot(mx,my,label='Mabbs17 Model')
plt.plot((12459.033,12459.033),(2500,-600),'C7--')
plt.plot((12440.77,12440.77),(2500,-600),'C7--')
plt.xlim(12380,12510)
plt.ylim(0,2200)
plt.xlabel('energy (cm$^{-1}$)')
plt.yticks([])
plt.legend()
plt.show()
