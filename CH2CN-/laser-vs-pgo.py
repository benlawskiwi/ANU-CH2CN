import numpy as np
import matplotlib.pyplot as plt

w1, sc1 = np.loadtxt('CH2CN-laserscan_25_06_20n3.dat', unpack=True)
w2, sc2 = np.loadtxt('CH2CN-laserscan_25_06_20n4.dat', unpack=True)
w3, sc3 = np.loadtxt('CH2CN-laserscan_26_06_20n1.dat', unpack=True)

w1 =  (w1-w1[0])*(799.691-805.223)/(w1[-1]-w1[0]) + 805.223
w2 =  (w2-w2[0])*(806.841-804.917)/(w2[-1]-w2[0]) + 804.917
w3 =  (w3-w3[0])*(796.911-800.010)/(w3[-1]-w3[0]) + 800.010

cal = 1.1
w1 += cal
w2 += cal
w3 += cal

w1 = 1e7/w1
w2 = 1e7/w2
w3 = 1e7/w3

pgo = np.loadtxt('CH2CN-pgo.dat', unpack=True)
pgo = (pgo[0]+6, pgo[1]*sc1.max()/pgo[1].max())

EA = 12468

plt.plot(w1, sc1, label='25n3')
plt.plot(w2, sc2, label='25n4')
plt.plot(w3, sc3/2, label=r'26n3$\div2$')

plt.plot((EA, EA), (0, 700), 'C7-.', lw=1)
plt.annotate('EA', (EA+2, 600), color='C7', fontsize='large')

sub = pgo[0] < 12481
plt.plot(pgo[0][sub], pgo[1][sub], 'C3', lw=1, label='pgo')
sub = pgo[0] >= 12481
plt.plot(pgo[0][sub]+2.4, pgo[1][sub], 'C4', lw=1, label='pgo+2.4')

plt.xlabel('EX wavelength (nm)')
plt.ylabel('photoelectrons')
plt.axis(xmin=12370, xmax=12540, ymin=-5, ymax=800)
plt.legend(labelspacing=0.1, fontsize='small')

plt.savefig('laser-vs-pgo.pdf')
plt.show()
