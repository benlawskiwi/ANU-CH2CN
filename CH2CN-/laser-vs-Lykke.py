import numpy as np
import matplotlib.pyplot as plt

w1, sc1 = np.loadtxt('CH2CN-laserscan_25_06_20n3.dat', unpack=True)
w2, sc2 = np.loadtxt('CH2CN-laserscan_25_06_20n4.dat', unpack=True)
w3, sc3 = np.loadtxt('CH2CN-laserscan_26_06_20n1.dat', unpack=True)
w4, sc4 = np.loadtxt('CH2CN-laserscan_29_06_20n1.dat', unpack=True)
w5, sc5 = np.loadtxt('CH2CN-laserscan_29_06_20n2.dat', unpack=True)
w6, sc6 = np.loadtxt('CH2CN-laserscan_29_06_20n3.dat', unpack=True)

w1 =  (w1 - w1[0])*(799.691 - 805.223)/(w1[-1] - w1[0]) + 805.223
w2 =  (w2 - w2[0])*(806.841 - 804.917)/(w2[-1] - w2[0]) + 804.917
w3 =  (w3 - w3[0])*(796.911 - 800.010)/(w3[-1] - w3[0]) + 800.010
w4 =  (w4 - w4[0])*(804.770 - 809.013)/(w4[-1] - w4[0]) + 809.013
w5 =  (w5 - w5[0])*(800.489 - 801.496)/(w5[-1] - w5[0]) + 801.496
w6 =  (w6 - w6[0])*(696.251 - 694.350)/(w6[-1] - w6[0]) + 694.350

cal = 1.7
w1 += cal
w2 += cal
w3 += cal
w4 += cal
w5 += cal
w6 -= 0.7

w1 = 1e7/w1
w2 = 1e7/w2
w3 = 1e7/w3
w4 = 1e7/w4
w5 = 1e7/w5
w6 = 1e7/w6

lykke = np.loadtxt('Lykke.csv', unpack=True)

EA = 12468

axd = plt.figure(constrained_layout=True).subplot_mosaic(
        """
        IIS
        """,
        gridspec_kw={'hspace': 0.3}
        )
axd['I'].plot(w1, sc1, label='25n3')
axd['I'].plot(w2, sc2, label='25n4')
axd['I'].plot(w3, sc3/2, label=r'26n3$\div2$')
axd['I'].plot(w4, sc4, label=r'29n1')
axd['I'].plot(w5, sc5/1.5, label=r'29n2$\div1.5$')

axd['I'].plot((EA, EA), (0, 700), 'C7-.', lw=1)
axd['I'].annotate('EA', (EA+2, 500), color='C7', fontsize='large')

axd['I'].plot(lykke[0]-5.5, (lykke[1]-lykke[1][-1])+100, '--', lw=1,
         label=r'Lykke$-5.5$cm$^{-1}$')

axd['I'].set_xlabel(r'EX idler+1.7nm (cm$^{-1}$)')
axd['I'].set_ylabel('photoelectrons')
axd['I'].set_xticks([12350, 12400, 12450, 12500])
axd['I'].axis(xmin=12330, xmax=12530, ymin=20, ymax=600)
axd['I'].legend(labelspacing=0.1, fontsize='small')

axd['S'].set_xlabel(r'EX signal-0.7nm (cm$^{-1}$)')
axd['S'].plot(w6, sc6, label=r'29n3')
axd['S'].legend(labelspacing=0.1, fontsize='small')

plt.savefig('laser-vs-Lykke.pdf')
plt.show()
