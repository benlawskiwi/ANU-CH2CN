import numpy as np
import matplotlib.pyplot as plt

PES = np.loadtxt('CH2CN-12F1CMI1536PESBE.dat', unpack=True)
PES2 = np.loadtxt('../../768.55nm/8Feb19/CH2CN-8F1CMI1536PESBE.dat', unpack=True)
PES3 = np.loadtxt('../../768.45nm/7Feb19/CH2CN-7F2CMI1536PESBE.dat', unpack=True)
PES4 = np.loadtxt('../../768.35nm/7Feb19/CH2CN-7F1CMI1536PESBE.dat', unpack=True)

plt.plot(*PES, lw=1, label='768.65nm')
plt.plot(*PES2, lw=1, label='768.55nm')
plt.plot(*PES3, lw=1, label='768.45nm')
plt.plot(*PES4, lw=1, label='768.35nm')

plt.axis(xmin=11800)
plt.title(r'CH$_2$CN$^-$ 768+nm')
plt.xlabel('eBE (cm$^{-1}$)')

plt.savefig('CH2CN-728nm.pdf', bb_inches='tight')
plt.show()
