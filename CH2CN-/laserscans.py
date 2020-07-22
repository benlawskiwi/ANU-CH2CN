import numpy as np
import matplotlib.pyplot as plt

w1, sc1 = np.loadtxt('CH2CN-laserscan_25_06_20n3.dat', unpack=True)
w2, sc2 = np.loadtxt('CH2CN-laserscan_25_06_20n4.dat', unpack=True)
w3, sc3 = np.loadtxt('CH2CN-laserscan_26_06_20n1.dat', unpack=True)
w4, sc4 = np.loadtxt('CH2CN-laserscan_29_06_20n1.dat', unpack=True)
w5, sc5 = np.loadtxt('CH2CN-laserscan_29_06_20n2.dat', unpack=True)

w1 =  (w1 - w1[0])*(801.451 - 807.037)/(w1[-1] - w1[0]) + 807.037
w2 =  (w2 - w2[0])*(808.668 - 806.732)/(w2[-1] - w2[0]) + 806.732
w3 =  (w3 - w3[0])*(798.664 - 801.772)/(w3[-1] - w3[0]) + 801.772
w4 =  (w4 - w4[0])*(806.557 - 810.826)/(w4[-1] - w4[0]) + 810.826
w5 =  (w5 - w5[0])*(802.261 - 803.274)/(w5[-1] - w5[0]) + 803.274

#Calculated Ratios/Shifts
sc3 *= 0.4866023579849946
w3 += 0.02569911
sc2 *= 0.7163461538461539
sc4 -= 22.537499999999994
sc4 *= 1.1981193357761366
w4 += 0.009

#Cut points
subr = np.logical_and(w3>0,w3 < 801.642)
w3 = w3[subr]
sc3 = sc3[subr]
subr = np.logical_and(w1>801.642,w1<806.862)
w1 = w1[subr]
sc1 = sc1[subr]
subr = np.logical_and(w2>806.872,w2<900)
w2 = w2[subr]
sc2 = sc2[subr]
subr = np.logical_and(w4>808.658,w4<900)
w4 = w4[subr]
sc4 = sc4[subr]

#Combine data
w3 = w3[::-1]
w1 = w1[::-1]
w4 = w4[::-1]
sc3 = sc3[::-1]
sc1 = sc1[::-1]
sc4 = sc4[::-1]
datax = np.concatenate((w3,w1,w2,w4))
datay = np.concatenate((sc3,sc1,sc2,sc4))
np.savetxt('ANUscan.dat',np.column_stack((datax,datay)),delimiter=',')

#Baseline correction
#subr = np.logical_and(w2>808.071,w2<808.393)
#k1 = sc2[subr]
#subr = np.logical_and(w4>808.071,w4<808.393)
#k2 = sc4[subr]
#ofs = np.mean(k2)-np.mean(k1)
#sc4 -= ofs
#print('offset')
#print(ofs)

#Calculating Normalizing intensities
#subr = np.logical_and(w2>808.44,w2<808.562)
#x1 = w2[subr]
#z1 = sc2[subr]
#subr = np.logical_and(w4>808.44,w4<808.562)
#x2 = w4[subr]
#z2 = sc4[subr]
#a = max(z1)
#b = max(z2)
#print(a)
#print(b)
#ratio = a/b

#Calculating calibration shifts
#subi = np.logical_and(z1>a-0.00001,z1<10000)
#xx = x1[subi]
#print(xx)
#subi = np.logical_and(z2>b-0.00001,z2<10000)
#yy = x2[subi]
#print(yy)
#shift = xx-yy
#sc2 *= ratio
#w3 += shift
#print('ratio')
#print(ratio)
#print('shift')
#print(shift)


plt.plot(w1,sc1,label='25n3')
plt.plot(w2,sc2,label='25n4')
plt.plot(w3,sc3,label='26n1')
plt.plot(w4,sc4,label='29n1')
#plt.plot(w5,sc5,label='29n2')
plt.plot(datax,datay+600,'k')
plt.legend()
plt.show()

#plt.plot(x1,z1)
#plt.plot(x2,z2)
#plt.show()

