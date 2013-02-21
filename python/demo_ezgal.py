#!/usr/bin/env python
import ezgal
import matplotlib.pyplot as plt

m=ezgal.ezgal('p2_ssp_z_0.02_salp.model')
m.add_filter('wfc3_f160w')
zf=3.0
zs=m.get_zs(zf)
plt.subplot(1,2,2)
plt.plot(zs,m.get_apparent_mags(zf,filters='sloan_i',zs=zs),'k-',label='sloan i')
plt.plot(zs,m.get_apparent_mags(zf,filters='ks',zs=zs),'r--',label='2MASS Ks')
plt.plot(zs,m.get_apparent_mags(zf,filters='ch2',zs=zs),'b:',label='IRAC ch2')
plt.xlabel('z')
plt.ylabel('Mag')
plt.subplot(1,2,2)
plt.plot(zs,m.get_rest_ml_ratios(zf,filters='sloan_i',zs=zs),'k-',label='sloan i')
plt.plot(zs,m.get_rest_ml_ratios(zf,filters='ks',zs=zs),'r--',label='2MASS Ks')
plt.plot(zs,m.get_rest_ml_ratios(zf,filters='ch2',zs=zs),'b:',label='IRAC ch2')
plt.xlabel('z')
plt.ylabel('M/L ratio')
plt.legend()
plt.show()

