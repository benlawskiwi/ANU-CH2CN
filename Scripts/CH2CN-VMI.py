import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('CH2CN-VMI-799.dat',unpack=True)

plt.plot(x,y,'C2')
plt.xlim(12200,12500)
plt.xlabel('Binding Energy (cm$^{-1}$)')
plt.ylabel('intensity (arb. u.)')
plt.title('CH$_2$CN$^-$ VMI at 799.805nm')
plt.show()
