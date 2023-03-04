
import numpy as np
import pandas as pd

# Library for thermal remote sensing and related physical equations

# Constants
STEFAN_BOLTZ = 5.670374419e-8   # W / m^2 / K^4
PLANCKS = 6.62607015e-34        # J / s
C_VACC = 299792458                  # m / s
BOLTZ = 1.380649e-23            # J / K
PI = 3.14159265359


# Temperature unit conversion helper functions
def tempCToK(T):
    return float(T)+273.15
def tempFToC(T):
    return (float(T)-32)*5/9


# Radiance / Hz from Radiance / m
def getRadianceFreq(radiance_wavelength, wavelength):
    return radiance_wavelength * wavelength**2 / C_VACC
# Radiance / Hz from Radiance / m
def getRadianceWavenum(radiance_wavelength, wavelength):
    return radiance_wavelength * wavelength**2


# Thermal Exitance
#   Takes temperature in K
#   Outputs emittance in W/m^2
def getTotalExitance(emissivity, temp):
    return STEFAN_BOLTZ*float(emissivity)*float(temp)**4
# Thermal Broadband Emissivity
#   Takes temperature in K
#   Takes exitance in W/m^2
def getTotalEmissivity(exitance, temp):
    return float(exitance) / STEFAN_BOLTZ / float(temp)**4
# Radiometric temperature
#   Takes kinetic temperature in K
#   Outputs radiometric temperature in K
def getRadTemp(emissivity, temp_kinetic, emissivity_radiometer=1):
    return (emissivity / emissivity_radiometer * temp_kinetic**4)**0.25
# Kinetic temperature from radiant temperature
#   Takes radiative temperature in K
#   Outputs kinetic temperature in K
def getTempFromRadTemp(emissivity, temp_rad, emissivity_radiometer=1):
    return (emissivity_radiometer / emissivity * temp_rad**4)**0.25
# Kinetic temperature from emissivity and emittance
#   Takes emittance in W/m^2
#   Outputs temperature in K
def getTempFromEmittance(emissivity, emittance):
    return (emittance / emissivity * STEFAN_BOLTZ) ** .25

# Get the total emitted and reflected radaition from the environment.
#   temp of the object is in K
#   temp_env of the environment is in K
def getEmittanceAndReflectanceTEnv(emissivity, temp, temp_env):
    return STEFAN_BOLTZ*(emissivity*temp**4 + (1-emissivity)*temp_env**4)

# Get irradiance from exitance and geometry for a spherical light source
#   assumes r_source and r_detector have the same units
#   outputs in same units as emittance
#   r_source is the radius of the source object
#  r_detector is the distance from the center of the source to the detector
def getIrradianceFromEmittance(emittance, r_source, r_detector):
    return emittance * (r_source / r_detector)**2

# Exitance of a mixed pixel
#   Takes temp_1 and temp_2 in K
#   Outputs exitance in W/m^2
def getMixedExitance(emissivity_1, emissivity_2, frac_1, frac_2, temp_1, temp_2):
    return frac_1*emissivity_1*STEFAN_BOLTZ*temp_1**4 + frac_2*emissivity_2*STEFAN_BOLTZ*temp_2**4

# Color temperature
#   Assumes wavelength is in meters
#   Outputs temperature in Kelvin
def getColorTemperature(wavelength):
    return 2.89779e-3 / wavelength

# Brightness Temperature
#   Assumes wavelength is in m
#   Assumes radiance is in W / m^2 / sr / m --> NOTE uses wavelength in m
def getBrightnessTemp(radiance, wavelength, emissivity=1):
    y = 2 * PLANCKS * C_VACC**2 / float(radiance/emissivity) / float(wavelength)**5
    print(y)
    return PLANCKS * C_VACC / BOLTZ / float(wavelength) / np.log(1 + y)
# Radiance at a wavelength
#   Assumes wavelength is in m
#   Assumes temperature is in K
#   Assumes emissivity = 1 by default
#   Outputs radiance in W / m^2 / sr / m ******* NOTE - PER METER *******
def getSpectralRadiance(wavelength, temperature, emissivity=1):
    x = PLANCKS * C_VACC / BOLTZ / float(wavelength) / float(temperature)
    print(x)
    return emissivity * 2 * PLANCKS * C_VACC**2 / float(wavelength)**5 / (np.exp(x) - 1)

# Equilibrium temperature based on incoming radiation, albedo, and emissivity
#   Takes irradiance values in W/m^2
#   Takes albedo and emissivity as dimensionless values from 0 to 1
#   Returns temperature in K
#  *** NOTE *** assumes incoming radiation is absorbed onver only one cross sectional area and emissivity is over entire target surface
def getEquilibriumTemp(irradiance_short, irradiance_long, albedo, emissivity):
    return (((1-float(albedo))*irradiance_short + emissivity*irradiance_long) / emissivity / STEFAN_BOLTZ / 4) ** 0.25
