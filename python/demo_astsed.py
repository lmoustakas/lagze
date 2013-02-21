#!/usr/bin/env python
from astLib import astSED as ad
m05ssp=ad.M05Model('/Users/leonidas/research/data/SSPs/Maraston2005/csp_e1.75_z001_salp.sed_agb')
m05ssp.ages
m05ssp.wavelengths
redshiftedm05ssp = m05ssp.getSED(1.0)


