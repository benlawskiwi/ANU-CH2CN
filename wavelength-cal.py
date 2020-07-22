import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

OPO = input("Enter OPO Idler Wavelength (800.000):")

x = [785.800,789.220,796.911,799.691,799.805,800.010,802.280,804.917,805.223,806.841,815.000]
y = [787.561,790.988,798.664,801.451,801.567,801.772,804.058,806.732,807.037,808.668,816.892]
d = [0.00138,0.00183,0.00226,0.00186,0.00271,0.00071,0.00257,0.00073,0.00093,0.00230,0.00217]

def func(x,b,a,m,c):
    return b*x**3+a*x**2+m*x+c

popt, pcov = curve_fit(func, x, y)

#print(popt[0])
#print(popt[1])

z = []
for i in range(0,np.size(x)):
    z.append(func(x[i],*popt))

wm = func(float(OPO),*popt)
print('WM wavelength: ')
print(wm)


plt.plot(x,z)
plt.errorbar(x,y,yerr=d,fmt='*',color='C2')
plt.xlabel('OPO Wavelength (nm)',fontsize=14)
plt.ylabel('High Finess Wave Meter Wavelength (nm)',fontsize=14)
plt.show()
