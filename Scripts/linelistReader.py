from numpy import *
import matplotlib.pyplot as plt

Jdd,Jd,Kdd,Kd,dJ,dK,dE,I = loadtxt('linelist.dat',unpack=True)
x,y = loadtxt('ANUscan.dat',delimiter=',',unpack=True)
x = 1e7/x
y -= 100

#Fitting Parameters
T = 150
amp = 1
EA = 12468
DBS = 39
FWHM = 2

#Anion Ground State
Add = 9.29431
Bdd = 0.338427
Cdd = 0.327061

#Dipole Bound State
Ad = 9.51035  #Lineberger
Bd = 0.341049
Cd = 0.328764

#Detachment Threshold
D0 = 39      #Neumark

def Gauss (E0,FWHM,E):
    alpha = FWHM/2/sqrt(log(2.0))
    return exp(-((E-E0)/alpha)**2)

def En (J,K,A,B,C):
    E = (B+C)/2*J*(J+1)+(A-(B+C))*K**2
    return E

def Boltz (E,T,J):
    P = (2*J+1)*exp(-(E/ev)/(T*kb))
    return P

#Plot parts of linelist to decode spectra

Ev = arange(EA-200,EA+200,0.01)
spec = zeros(size(Ev))
n = size(Jdd)
for i in range(0,n):
    jdd = Jdd[i]
    kdd = Kdd[i]
    jd = Jd[i]
    kd = Kd[i]
    dj = dJ[i]
    dk = dK[i]
    de = dE[i]
    ii = I[i]
    if jd == 5:
        spec += amp*ii*Gauss(de,FWHM,Ev)

plt.plot(x,y)
plt.plot(Ev,spec,'C3')
plt.show()
