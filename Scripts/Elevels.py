import numpy as np
import matplotlib.pyplot as plt

Ad = 9.29431
Bd = 0.338427
Cd = 0.327061

Add = 9.51035
Bdd = 0.341049
Cdd = 0.328764

def rot (J,K,A,B,C):
    E = (B+C)/2*J*(J+1)+(A-(B+C))*K**2
    return E

#Kdd=0
Jdd0 = np.arange(0,20,1)
Edd0 = rot(Jdd0,0,Add,Bdd,Cdd)
#Kdd=1
Jdd1 = np.arange(1,20,1)
Edd1 = rot(Jdd1,1,Add,Bdd,Cdd)
#Kdd=2
Jdd2 = np.arange(2,20,1)
Edd2 = rot(Jdd2,2,Add,Bdd,Cdd)
#Kdd=3
Jdd3 = np.arange(3,20,1)
Edd3 = rot(Jdd3,3,Add,Bdd,Cdd)

for i in range(0,np.size(Jdd0)):
    plt.plot((0,1),(Edd0[i],Edd0[i]),'C0')
    plt.annotate(i,(-0.20,Edd0[i]),ha='left')
for i in range(0,np.size(Jdd1)):
    plt.plot((2,3),(Edd1[i],Edd1[i]),'C1')
    plt.annotate(i+1,(1.80,Edd1[i]),ha='left')
for i in range(0,np.size(Jdd2)):
    plt.plot((4,5),(Edd2[i],Edd2[i]),'C2')
    plt.annotate(i+2,(3.80,Edd2[i]),ha='left')
for i in range(0,np.size(Jdd3)):
    plt.plot((6,7),(Edd3[i],Edd3[i]),'C3')
    plt.annotate(i+3,(5.80,Edd3[i]),ha='left')

plt.plot((-0.5,7),(39,39),'C7--')
plt.annotate('K$_a$=0',(0.5,-8),ha='center')
plt.annotate('K$_a$=1',(2.5,-8),ha='center')
plt.annotate('K$_a$=2',(4.5,-8),ha='center')
plt.annotate('K$_a$=3',(6.5,-8),ha='center')
plt.annotate('J',(-0.1,Edd0[-1]+10),ha='left')
plt.annotate('J',(1.8,Edd1[-1]+10),ha='left')
plt.annotate('J',(3.8,Edd2[-1]+10),ha='left')
plt.annotate('J',(5.9,Edd3[-1]+10),ha='left')
plt.annotate('Detachment Threshold',(6.5,42),ha='center')
plt.annotate('$\sim39~$cm$^{-1}$',(6.5,30),ha='center')
plt.ylabel('Energy of rotational level (cm$^{-1}$)')
plt.xlabel('CH$_2$CN$^-$ dipole bound state')
plt.xticks([])
#plt.plot(Jdd0,Edd0)
#plt.plot(Jdd1,Edd1)
#plt.plot(Jdd2,Edd2)
#plt.plot(Jdd3,Edd3)
plt.show()
energy = rot(1,0,Add,Bdd,Cdd)
print(energy)
