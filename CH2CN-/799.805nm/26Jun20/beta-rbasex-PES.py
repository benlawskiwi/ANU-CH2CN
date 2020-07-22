import numpy as np
import abel
import matplotlib.pylab as plt

sz = 512
imagefile = f'CH2CN-26J4CMbb{sz}.txt' 

IM = np.loadtxt(imagefile)
zoom = IM.shape[-1]/2048

# radial range of peak X origin intensity used for image centering
rr = (int(100*zoom), int(230*zoom))

'''
IMcm, ang, rc, rcf = abel.tools.circularize.circularize_image(
                     IM, inverse=False, origin='slice',
                     radial_range=rr, #  ref_angle=0,
                     return_correction=True, dt=0.05, tol=1)
'''

IMcm = abel.tools.center.center_image(IM, method='slice',
                                      radial_range=rr)

r, c = IMcm.shape
r2 = r//2
'''
plt.plot(np.arange(-r2, r2-1), IMcm[r2-50: r2+50].sum(axis=0))
plt.show()
'''

# mask
mask = np.ones_like(IMcm, dtype=int)
R, C = np.meshgrid(np.arange(c), np.arange(r))
subr = (R - 1051)**2 + (C - 1045)**2 < 20**2
mask[subr] = 0

# Abel transform - rbasex ------------------------------------------
# adjust reg parameter for smoothing
AIM = abel.Transform(IMcm, method='rbasex', 
                     transform_options=dict(reg=("diff", 1000),
                     basis_dir='./')) # weights=mask))

r, I, beta = AIM.distr.rIbeta()   # I, beta directly from basis fit

# convert intensity to PES
eBE, PES = abel.tools.vmi.toPES(r, I,
                                energy_cal_factor=1.15e-5,
                                photon_energy=1.0e7/799.805, Vrep=-100,
                                zoom=zoom)
beta = beta[::-1]

# normalize intensity to X origin
PES /= PES.max()

np.savetxt(f'{imagefile[:-4]}_rbasex.dat', np.column_stack((eBE, PES, beta)),
           fmt='%8.3f   %10.5f    %10.5f',
           header='eBE(cm-1)  int. (rel. X0)  beta')

# plots ----------------------------
EA = 12468
print(f'EA = {EA}')
peak = eBE[PES.argmax()]
print(f'peak = {peak}')
# eBE -= EA

wp, pgo = np.loadtxt('CH2CN-pgo.dat', unpack=True)

fig, ax = plt.subplots()

ax.plot(eBE, PES, label=r'PES')
ax.plot(eBE, PES*beta, lw=1, label=r'PES$\times\beta$')

subr = wp < eBE[-1]
ax.plot(wp[subr], pgo[subr]*.8/pgo[subr].max(), lw=1, label='pgo')
subr = wp-24 < eBE[-1]
ax.plot(wp[subr]-24, pgo[subr]*.5/pgo[subr].max(), lw=1, label='pgoDBS')

ax.plot((eBE[0], eBE[-1]), (0, 0), 'C7--')
ax.plot((EA, EA), (-0.5, 1.05), 'C7--')
ax.annotate(r'$EA$', (EA, 1.07), fontsize='large', ha='right')

ax.legend()
ax.set_xlabel(r'eBE (cm$^{-1}$)')
ax.set_ylabel(r'intensity (rel. $\tilde{X}$ origin)')
ax.set_title(imagefile)
ax.axis(xmin=12300, xmax=12600, ymin=-0.1, ymax=1.1)

plt.subplots_adjust(left=0.15)
plt.savefig('beta-rbasex-PES.png', dpi=100)
plt.show()
