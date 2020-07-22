from numpy import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

kb = 8.617333262145e-5
ev = 8065.74

hv = 801.5725
hv = 1e7/hv
tol = 1

#x,y = loadtxt('ANUscan.dat',delimiter=',',unpack=True)
x,y = loadtxt('CH2CN-VMI-799.dat',unpack=True)
x2,y2 = loadtxt('CH2CN-768nm.dat',unpack=True)
#x = 1e7/x
#Remove background
step = 10
n = round(size(x)/step)
xx = []
yy = []
for i in range(0,n-1):
    s = slice(step*i,step*i+step,1)
    a = mean(x[s])
    b = min(y[s])
    xx.append(a)
    yy.append(b)
bkg = mean(yy)
y -= bkg
#print(bkg)

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

def spectrum(Ev,T,FWHM,amp):
    #Set up spectrum
    #Ev = arange(EA-200,EA+200,0.1)
    spec = zeros(size(Ev))
    linelist = {}
    nu = EA-DBS
    #Selection rules/intensities                    (Jdd,Kdd) -> (Jd,Kd)
    for Jdd in range(0,12):
        for dJ in (-1,0,1):
            Jd = Jdd + dJ                           #dJ=0,=/-1
            if Jd <0 :continue
            for Kdd in range (0,Jdd+1):
                Edd = En(Jdd,Kdd,Add,Bdd,Cdd)
                I = Boltz(Edd,T,Jdd)
                if Kdd%2 !=0:
                    I *=3                           #Spin statistics 3:1
                for dK in (-1,1):                   #dK=+/-1
                    Kd = Kdd + dK
                    if Kd < 0: continue
                    if Kd > Jd : continue
                    if dJ == 1 and dK == 1: HL = (Jdd+2+Kdd)*(Jdd+1+Kdd)/((Jdd+1)*(2*Jdd+1))
                    if dJ == 1 and dK == -1: HL = (Jdd+2-Kdd)*(Jdd+1-Kdd)/((Jdd+1)*(2*Jdd+1))
                    if dJ == 0 and dK == 1: HL = (Jdd+1+Kdd)*(Jdd-Kdd)/(Jdd*(Jdd+1))
                    if dJ == 0 and dK == -1: HL = (Jdd+1-Kdd)*(Jd+Kdd)/(Jdd*(Jdd+1))
                    if dJ == -1 and dK == 1: HL = (Jdd-1-Kdd)*(Jdd-Kdd)/(Jdd*(2*Jdd+1))
                    if dJ == -1 and dK == -1: HL = (Jdd-1+Kdd)*(Jdd+Kdd)/(Jdd*(2*Jdd+1))
                    I *= HL #Honl-London Factors - perpendicular transition of a prolate symmetric top
                    Ed = En(Jd,Kd,Ad,Bd,Cd)
                    if Ed < D0: continue  #These lines won't autodetach
                    dE = Ed-Edd+nu
                    if dE > hv+tol: continue  #Autodtechment
                    if dE < hv-tol: continue
                    for dJn in (-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7):
                        Jn = Jd+dJ
                        if Jn <0 :continue
                        for dKn in (-2,0):
                            #if dKn == -2: continue
                            Kn = Kd+dKn
                            if Kn <0 :continue
                            if Kn > Jn : continue
                            Edn = En(Jn,Kn,Ad,Bd,Cd)
                            KE = Ed-Edn
                            BE = hv-KE
                            linelist[(Jd,Kd,Jn,Kn,dKn,dJn)] = (BE,amp*I)
                            spec += amp*I*Gauss(BE,FWHM,Ev)
    return (spec,linelist,Ev)

def fit(Ev,amp):            #Change amp to whatever parameter(s) you want to fit. Currently set for amp, T, FWHM, but easy to extend to others
    spec,linelist,Ev = spectrum(Ev,T,FWHM,amp)
    return spec

#Curve Fit
popt, pcov = curve_fit(fit,x,y)
#print(popt)


spec,linelist,Ev = spectrum(x,T,FWHM,amp)
print('(Jd,Kd,Jn,Kn,dKn,dJn) (BE,I)')
for line,posAmp in sorted(linelist.items(),key=lambda x: x[1][0]):
    print(line,posAmp)


#plt.plot(Ev,spec)
plt.plot(x,y)
plt.plot(x,fit(x,*popt),'C3')
#plot params
for i in range (0,size(popt)):
    x0 = 12350
    y0 = 500-50*i
    perr = sqrt(diag(pcov[i]))
    perrs=round(perr[0][0],3)
    st = 'param = '+str(round(popt[i],3))+' +/- '+str(perrs)
    plt.annotate(st,(x0,y0))

savetxt('threshold-set.dat',column_stack((x,fit(x,*popt))))

y2 /= 4
plt.plot(x2,y2)
plt.xlabel(r'energy (cm$^{-1}$)')
plt.ylabel('intensity (arb. u.)')
plt.show()

#plt.plot(x,y)
#plt.plot(x,test(x,*popt))
#plt.show()
