
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

PI = 3.1415927

def radFromDeg(deg):
    return float(deg)*PI/180
def degFromRad(rad):
    return float(rad)*180/PI

def getRefractionAngle(n_1, n_2, theta_1):
    return np.arcsin(float(n_1)/float(n_2)*np.sin(theta_1))

# Calculate absorption coefficient from extinction coefficient
def getAlphaFromK(k, wavelength):
    return 4.0*PI*float(k)/float(wavelength)
# Calculate absorption coefficient from extinction coefficient
def getKFromAlpha(alpha, wavelength):
    return float(alpha)*float(wavelength)/4.0/PI
# Calculate e-folding distance from wavelength and extinction coefficient
def getEFoldingDistance(k, wavelength):
    return 1.0/getAlphaFromK(k, wavelength)

# ***** Fresnel's Equations *****
# Parallel Portion
def getParallelReflFresnel(n_1, n_2, k_1, k_2, theta_0):
    theta_chi = getRefractionAngle(n_1, n_2, theta_0)
    p1 = (float(n_2)*np.cos(theta_0) - float(n_1)*np.cos(theta_chi))**2
    p2 = (float(k_2)*np.cos(theta_0) - float(k_1)*np.cos(theta_chi))**2
    p3 = (float(n_2)*np.cos(theta_0) + float(n_1)*np.cos(theta_chi))**2
    p4 = (float(k_2)*np.cos(theta_0) + float(k_1)*np.cos(theta_chi))**2
    return (p1 + p2) / (p3 + p4)
# Perpendicular Portion
def getPerpendicularReflFresnel(n_1, n_2, k_1, k_2, theta_0):
    theta_chi = getRefractionAngle(n_1, n_2, theta_0)
    p1 = (float(n_2)*np.cos(theta_chi) - float(n_1)*np.cos(theta_0))**2
    p2 = (float(k_2)*np.cos(theta_chi) - float(k_1)*np.cos(theta_0))**2
    p3 = (float(n_2)*np.cos(theta_chi) + float(n_1)*np.cos(theta_0))**2
    p4 = (float(k_2)*np.cos(theta_chi) + float(k_1)*np.cos(theta_0))**2
    return (p1 + p2) / (p3 + p4)
# Brewster Angle (angle where all reflected light is perpendicularly polarized)
def getBrewsterAngle(n):
    return np.arctan(n)
