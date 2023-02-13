
import numpy as np
import pandas as pd

# Library for thermal remote sensing and related physical equations

# Constants
STEFAN_BOLTZ = 5.670374419e-8   # W / m^2 / K^4
PLANCKS = 6.62607015e-34        # J / s
C_VACC = 3.0e8                  # m / s
BOLTZ = 1.380649e-23            # J / K

# Temperature unit conversion helper functions
def tempCToK(T):
    return float(T)+273.15
def tempFToC(T):
    return (float(T)-32)*5/9


# Thermal Exitance
#   Takes temperature in K
#   Outputs emittance in W/m^2
def getTotalEmittance(emissivity, temp):
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


# Exitance of a mixed pixel
#   Takes temp_1 and temp_2 in K
#   Outputs exitance in W/m^2
def getMixedExitance(emissivity_1, emissivity_2, frac_1, frac_2, temp_1, temp_2):
    return frac_1*emissivity_1*STEFAN_BOLTZ*temp_1**4 + frac_2*emissivity_2*STEFAN_BOLTZ*temp_2**4

# Brightness Temperature
#   Assumes wavelength is in m
#   Assumes radiance is in W / m^2 / sr / m --> NOTE uses wavelength in m
def getBrightnessTemp(radiance, wavelength, emissivity=1):
    y = 2 * PLANCKS * C_VACC**2 / float(radiance/emissivity) / float(wavelength)**5
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
def getEquilibriumTemp(irradiance_short, irradiance_long, albedo, emissivity):
    return (((1-float(albedo))*irradiance_short + emissivity*irradiance_long) / emissivity / STEFAN_BOLTZ) ** 0.25

print("")
print("For problem 4.1:")
print("Can exitance is: " + str(getTotalEmittance(0.07, tempCToK(7.5))) + " W/m^2")
print("Brick exitance is: " + str(getTotalEmittance(0.85, tempCToK(7.5))) + " W/m^2")
print("Glass exitance is: " + str(getTotalEmittance(0.92, tempCToK(7.5))) + " W/m^2")
print("Can " + str(getTempFromEmittance(1, getEmittanceAndReflectanceTEnv(0.07, 7.5+273.15, 500))))


print("")
print("For problem 4.2:")
measured_radiance_4p2 = getSpectralRadiance(8.9e-6, 328.15)
print("Measured radiance is: " + str(measured_radiance_4p2) + " W/m^2/m")
kinetic_temperature_4p2 = getBrightnessTemp(15550081.57774587, 8.9e-6, emissivity=0.64)
print("Kinetic temperature is " + str(kinetic_temperature_4p2) + " K")
total_emissivity_4p2 = getTotalEmissivity(844, 425.1)
print("Total emissivity is: " + str(total_emissivity_4p2))

print("")
print("For problem 4.3:")
print("Radiometric temperature of ice is " + str(getRadTemp(0.96, 260.14, 1)))
print("Radiometric temperature of cloud is " + str(getRadTemp(0.65, 240.0, 1)))
print("Mixed exitance is " + str(getMixedExitance(0.96, 0.65, 0.30, 0.70, 260.14, 240.0)))

print("")
print("For problem 4.4:")
print("Equilibrium temperature of Mars is: " + str(getEquilibriumTemp(589/4, (591.2-589)/4, 0.15, 0.96)) + " K")
print("Equilibrium temperature of the Musked Mars is: " + str(getEquilibriumTemp(589/4, (591.2-589)/4, 0.06, 0.98)) + " K")

print("")
print("For problem 4.5:")
print("Spectral radiance of forest at 3.7 um: " + str(getSpectralRadiance(3.7e-6, 303, 0.9)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of forest at 10.76 um: " + str(getSpectralRadiance(10.76e-6, 303, 0.9)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of fire at 3.7 um: " + str(getSpectralRadiance(3.7e-6, 1123, 1)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of fire at 10.76 um: " + str(getSpectralRadiance(10.76e-6, 1123, 1)*10**-6) + " W/m^2/sr/um")

print("Spectral radiance of the sun at 3.7 um: " + str(getSpectralRadiance(3.7e-6, 5800, 1)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of the sun at 10.76 um: " + str(getSpectralRadiance(10.76e-6, 5800, 1)*10**-6) + " W/m^2/sr/um")





#
