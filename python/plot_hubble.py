import numpy as np
import matplotlib.pyplot as plt 
import astropy.cosmology as cosmo 

'''
astropy.cosmology.FlatLambdaCDM(
    H0,
    Om0,
    Tcmb0=<Quantity 0. K>,
    Neff=3.04,
    m_nu=<Quantity 0. eV>,
    Ob0=None,
    *,
    name=None,
    meta=None,
)
'''

plt.ion()

params = [
          [ 0.27, 0.68, -1.0, 'C0-'],
          [ 0.31, 0.68, -1.0, 'C0--'],
          [ 0.35, 0.68, -1.0, 'C0:'], 
          [ 0.31, 0.73, -0.9, 'C3--'],
          [ 0.31, 0.73, -1.0, 'C3-'],
          [ 0.31, 0.73, -1.1, 'C3:']
          ]

plt.figure(figsize=(7.5, 5)) 
z = np.linspace(0, 3, 100)
for p in params:

    Om0 = p[0]
    H0 = p[1]*100 
    w0 = p[2]
    c = cosmo.FlatwCDM(H0, Om0, w0)

    label = '$\Omega_m = {Om0}$ $h = {h:.2f}$ $w_0= {w0}$'.format(Om0=Om0, h=p[1], w0=w0)
    plt.plot(z, c.H(z)/(1+z), p[3], lw=2, alpha=0.6, label=label)

plt.xlabel(r'Redshift $z$')
plt.ylabel(r'$\dot{a}(z) = H(z)/(1+z) \ \  [\mathrm{km} \, \mathrm{s}^{-1}\mathrm{Mpc}^{-1}]$')
plt.legend(ncol=2)
plt.tight_layout()
plt.savefig('hubble.pdf')