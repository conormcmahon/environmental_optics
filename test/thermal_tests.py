
import thermal_rs as ths
import numpy as np
import pandas as pd


print("")
print("For problem 4.1:")
print("Can exitance is: " + str(ths.getTotalExitance(0.07, ths.tempCToK(7.5))) + " W/m^2")
print("Brick exitance is: " + str(ths.getTotalExitance(0.85, ths.tempCToK(7.5))) + " W/m^2")
print("Glass exitance is: " + str(ths.getTotalExitance(0.92, ths.tempCToK(7.5))) + " W/m^2")
print("Can " + str(ths.getTempFromEmittance(1, ths.getEmittanceAndReflectanceTEnv(0.07, 7.5+273.15, 500))))


print("")
print("For problem 4.2:")
measured_radiance_4p2 = ths.getSpectralRadiance(8.9e-6, 328.15)
print("Measured radiance is: " + str(measured_radiance_4p2) + " W/m^2/m")
kinetic_temperature_4p2 = ths.getBrightnessTemp(15550081.57774587, 8.9e-6, emissivity=0.64)
print("Kinetic temperature is " + str(kinetic_temperature_4p2) + " K")
total_emissivity_4p2 = ths.getTotalEmissivity(844, 425.1)
print("Total emissivity is: " + str(total_emissivity_4p2))

print("")
print("For problem 4.3:")
print("Radiometric temperature of ice is " + str(ths.getRadTemp(0.96, 260.14, 1)))
print("Radiometric temperature of cloud is " + str(ths.getRadTemp(0.65, 240.0, 1)))
print("Mixed exitance is " + str(ths.getMixedExitance(0.96, 0.65, 0.30, 0.70, 260.14, 240.0)))

print("")
print("For problem 4.4:")
print("Equilibrium temperature of Mars is: " + str(ths.getEquilibriumTemp(589/4, (591.2-589)/4, 0.15, 0.96)) + " K")
print("Equilibrium temperature of the Musked Mars is: " + str(ths.getEquilibriumTemp(589/4, (591.2-589)/4, 0.06, 0.98)) + " K")

print("")
print("For problem 4.5:")
print("Spectral radiance of forest at 3.7 um: " + str(ths.getSpectralRadiance(3.7e-6, 303, 0.9)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of forest at 10.76 um: " + str(ths.getSpectralRadiance(10.76e-6, 303, 0.9)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of fire at 3.7 um: " + str(ths.getSpectralRadiance(3.7e-6, 1123, 1)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of fire at 10.76 um: " + str(ths.getSpectralRadiance(10.76e-6, 1123, 1)*10**-6) + " W/m^2/sr/um")

print("Spectral radiance of the sun at 3.7 um: " + str(ths.getSpectralRadiance(3.7e-6, 5800, 1)*10**-6) + " W/m^2/sr/um")
print("Spectral radiance of the sun at 10.76 um: " + str(ths.getSpectralRadiance(10.76e-6, 5800, 1)*10**-6) + " W/m^2/sr/um")




print("")
print("")
print("")
print("")
print("")
print(" Lab 3...")
print("   Solar Emittance at Select Wavelengths:")
solar_emit_5 = ths.getSpectralRadiance(0.5e-6, 5800, 1) * np.pi
solar_emit_6 = ths.getSpectralRadiance(0.6e-6, 5800, 1) * np.pi
solar_emit_9 = ths.getSpectralRadiance(0.9e-6, 5800, 1) * np.pi
print("Exitance of the sun at 0.5 um: " + str(solar_emit_5*10**-6) + " W/m^2/sr/um")
print("Exitance of the sun at 0.6 um: " + str(solar_emit_6*10**-6) + " W/m^2/sr/um")
print("Exitance of the sun at 0.9 um: " + str(solar_emit_9*10**-6) + " W/m^2/sr/um")
print("   Solar Irradiance at the Ground:")
print("Irradiance of the sun at 0.5 um: " + str(ths.getIrradianceFromEmittance(solar_emit_5, 6.97e8, 1.49e11)*10**-6) + " W/m^2/sr/um")
print("Irradiance of the sun at 0.6 um: " + str(ths.getIrradianceFromEmittance(solar_emit_6, 6.97e8, 1.49e11)*10**-6) + " W/m^2/sr/um")
print("Irradiance of the sun at 0.9 um: " + str(ths.getIrradianceFromEmittance(solar_emit_9, 6.97e8, 1.49e11)*10**-6) + " W/m^2/sr/um")





print("")
print("")
print("")
print("*************************************************")
print("OK!! Midterm Time!")
print("")
print("Q1")
print("  Radiance per frequency: " + str(ths.getRadianceFreq(3.4e6, 11.5e-6)))
print("  Expected radiance from a blackbody at 11.5 um: " + str(ths.getSpectralRadiance(11.5e-6, 243, 1)) + " W/m^2/m/sr")
print("  Emissivity at 11.5 um: " + str(3.4e6 / ths.getSpectralRadiance(11.5e-6, 243, 1)))
print("  Brightness temperature at 11.5 um: " + str(ths.getBrightnessTemp(3.4e6, 11.5e-6, 1)) + " K")
print("")
print("Q2")
color_temp_star = ths.getColorTemperature(652.6e-9)
print("  Color Tempearture is: " + str(color_temp_star))
total_exitance = ths.getTotalExitance(1, color_temp_star)
print("  Exitance for the star is: " + str(total_exitance))
print("   Thermal Equilibrium at close distance: " + str(ths.getEquilibriumTemp(ths.getIrradianceFromEmittance(total_exitance,4.87e5,6.9e6)*0.958,
                                                                            ths.getIrradianceFromEmittance(total_exitance,4.87e5,6.9e6)*(1-0.958),
                                                                            0.25,
                                                                            0.92)))
print("   Thermal Equilibrium at far distance: " + str(ths.getEquilibriumTemp(ths.getIrradianceFromEmittance(total_exitance,4.87e5,1.05e7)*0.958,
                                                                            ths.getIrradianceFromEmittance(total_exitance,4.87e5,1.05e7)*(1-0.958),
                                                                            0.25,
                                                                            0.92)))
print("")
print("Q5")
equil_temp = ths.getEquilibriumTemp(1360, 1372-1360, 0.3, 0.95)
print("  Thermal Equilibrium Temperature for current Earth: " + str(equil_temp))
print("  Thermal Equilibrium Temperature for current Earth: " + str(ths.getEquilibriumTemp(1360*(1307/1372), (1372-1360)*(1307/1372), 0.3, 0.95)))
print("  Thermal Equilibrium Temperature for current Earth: " + str(ths.getEquilibriumTemp(1360*(1436/1372), (1372-1360)*(1436/1372), 0.3, 0.95)))
post_eruption_temp = ths.getEquilibriumTemp(1360, 1372-1360, 0.3323, 0.95)
print("  To double check, with albedo = 0.6677 the new equilibrium temperature for Earth is: " + str(post_eruption_temp))
print("  That results in a temperature difference of: " + str(equil_temp-post_eruption_temp))

print("")
print("Q6")
solar_exitance_0p6 = ths.getSpectralRadiance(0.6e-6, 5772, 1.0)
solar_exitance_10p = ths.getSpectralRadiance(10.0e-6, 5772, 1.0)
print("  Solar exitance at 0.6 um is:  " + str(solar_exitance_0p6*10**-6) + " W/m^2/sr/um")
print("  Solar exitance at 10.0 um is: " + str(solar_exitance_10p*10**-6) + " W/m^2/sr/um")
solar_irradiance_0p6 = np.pi * ths.getIrradianceFromEmittance(solar_exitance_0p6, 6.97e8, 1.49e11)
solar_irradiance_10p = np.pi * ths.getIrradianceFromEmittance(solar_exitance_10p, 6.97e8, 1.49e11)
print("  Solar irradiance at 0.6 um is:  " + str(solar_irradiance_0p6*10**-6) + "W/m^2/sr/um")
print("  Solar irradiance at 10.0 um is: " + str(solar_irradiance_10p*10**-6) + "W/m^2/sr/um")
greenhouse_exitance_10p = np.pi * ths.getSpectralRadiance(10.0e-6, 28+273.15, 0.95)
print("  Greenhouse exitance at 10.0 um is: " + str(greenhouse_exitance_10p*10**-6) + " W/m^2/sr/um")


#
