
import refraction as refr
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


viewing = np.linspace(-75, 75, 100)
oak_nir = 0.25 + (viewing-20) * 0.04 / 150
oak_red = 0.05 + (viewing-20) * 0.075 / 150
chap_nir = 0.2 + (viewing-20) * 0.02 / 150
chap_red = 0.05 + (viewing-20) * 0.05 / 150
grass_nir = 0.25 + (viewing-20) * 0.01 / 150
grass_red = 0.05 + (viewing-20) * 0.025 / 150


# Set up plot, add lines
fig, ax = plt.subplots(1,1)
ax.plot(viewing, oak_nir, 'g-')
ax.plot(viewing, oak_red, 'r-')
ax.plot(viewing, chap_nir, 'g--')
ax.plot(viewing, chap_red, 'r--')
ax.plot(viewing, grass_nir, 'g.')
ax.plot(viewing, grass_red, 'r.')
# Captions and Axis labels
plt.xlabel("Viewing Angle")
plt.ylabel("Log of Negative Rate of Change in Radiance log(W/m^2/sr/um/m)")
# Set axis tick marks and grid parameters
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(5))
ax.set_ylim([0.0, 0.5])
plt.grid(color="gray", linestyle="--")

fig.tight_layout(pad=1)

r_series = np.array([0,0.3])
plane_south = np.array([-17,-17])*np.pi/180
plane_north = np.array([17,17])*np.pi/180
sun_angle = np.array([-20,-20])*np.pi/180

# Set up plot
fig, (ax_polar_nir, ax_polar_red) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
ax_polar_nir.plot(viewing * (3.14159/180), oak_nir, 'g-')
ax_polar_nir.plot(viewing * (3.14159/180), chap_nir, 'k-')
ax_polar_nir.plot(viewing * (3.14159/180), grass_nir, 'r-')
ax_polar_nir.plot(plane_south, r_series, 'c--')
ax_polar_nir.plot(plane_north, r_series, 'c--')
ax_polar_nir.plot(sun_angle, r_series, 'y--')
ax_polar_nir.set_rticks([0,0.1,0.2,0.3,0.4,0.5])
ax_polar_nir.set_xticks(np.pi/180. * np.linspace(-90,  90, 13, endpoint=True))
ax_polar_nir.text(-3.14159*(0.72),ax_polar_nir.get_rmax()*0.6,"Theoretical Irradiance",
                ha='center',va='center')
ax_polar_nir.set_rlabel_position(120)  # Move radial labels away from plotted line
ax_polar_nir.grid(True)
ax_polar_nir.set_title("Lambertian", va='bottom')
ax_polar_nir.set_thetamin(-90)
ax_polar_nir.set_thetamax(90)
ax_polar_nir.set_theta_zero_location("N")

ax_polar_red.plot(viewing * (3.14159/180), oak_red, 'g-')
ax_polar_red.plot(viewing * (3.14159/180), chap_red, 'k-')
ax_polar_red.plot(viewing * (3.14159/180), grass_red, 'r-')
ax_polar_red.plot(plane_south, r_series, 'c--')
ax_polar_red.plot(plane_north, r_series, 'c--')
ax_polar_red.plot(sun_angle, r_series, 'y--')
ax_polar_red.set_rticks(np.array([0,0.1,0.2,0.3,0.4,0.5])/2.0)
ax_polar_red.set_xticks(np.pi/180. * np.linspace(-90,  90, 13, endpoint=True))
ax_polar_red.text(-3.14159*(0.72),ax_polar_red.get_rmax()*0.6,"Theoretical Irradiance",
                ha='center',va='center')
ax_polar_red.set_rlabel_position(120)  # Move radial labels away from plotted line
ax_polar_red.grid(True)
ax_polar_red.set_title("Lambertian", va='bottom')
ax_polar_red.set_thetamin(-90)
ax_polar_red.set_thetamax(90)
ax_polar_red.set_theta_zero_location("N")

#   Print plot
plt.savefig("brdf_hypothetical.png")




print("")
print("")

print("Question 1.1 - Supporting refraction math:")
red_theta_2 = refr.degFromRad(refr.getRefractionAngle(1.00, 1.455, refr.radFromDeg(60)))
red_theta_3 = refr.degFromRad(refr.getRefractionAngle(1.47, 1.00, refr.radFromDeg(red_theta_2-refr.radFromDeg(60))))
print(" Incoming red light is first refracted from 60° off-normal to " + str(refr.degFromRad(refr.getRefractionAngle(1.00, 1.47, refr.radFromDeg(60)))) + "° off-normal")
print(" Then, the red light is refracted from " + str(red_theta_2) + "° off-normal to " + str(refr.degFromRad(refr.getRefractionAngle(1.00, 1.47, refr.radFromDeg(60)))) + "° off-normal")
print("")


print("Question 1.2 - Supporting refraction math:")
print(refr.degFromRad(refr.getRefractionAngle(1.00, 1.47, refr.radFromDeg(60))))
print(refr.degFromRad(refr.getRefractionAngle(1.00, 1.455, refr.radFromDeg(60))))
print("")


print("Question 5.3")
e_fold_dist_48 = refr.getEFoldingDistance(9.33e-10, 0.48e-6)
e_fold_dist_60 = refr.getEFoldingDistance(1.17e-8, 0.60e-6)
e_fold_dist_70 = refr.getEFoldingDistance(3.62e-8, 0.70e-6)
print("   For a wavelength of 0.48 um with k=9.33e-10, e-folding dist is    " + str(e_fold_dist_48) + " m")
print("   For a wavelength of 0.60 um with k=1.17e-8, e-folding dist is    " + str(e_fold_dist_60) + " m")
print("   For a wavelength of 0.70 um with k=3.62e-8, e-folding dist is    " + str(e_fold_dist_70) + " m")
print("")
theta_chi_48 = refr.getRefractionAngle(1.0, 1.336, refr.radFromDeg(15))
theta_chi_60 = refr.getRefractionAngle(1.0, 1.333, refr.radFromDeg(15))
theta_chi_70 = refr.getRefractionAngle(1.0, 1.330, refr.radFromDeg(15))
print("   For a wavelength of 0.48 um with n=1.336 and theta_0 = 15°, theta_chi = " + str(refr.degFromRad(theta_chi_48)) + " °")
print("   For a wavelength of 0.60 um with n=1.333 and theta_0 = 15°, theta_chi = " + str(refr.degFromRad(theta_chi_60)) + " °")
print("   For a wavelength of 0.70 um with n=1.330 and theta_0 = 15°, theta_chi = " + str(refr.degFromRad(theta_chi_70)) + " °")
print("")
path_1m_48 = 1 / np.cos(theta_chi_48)
path_2m_48 = 2 / np.cos(theta_chi_48)
path_5m_48 = 5 / np.cos(theta_chi_48)
path_1m_60 = 1 / np.cos(theta_chi_60)
path_2m_60 = 2 / np.cos(theta_chi_60)
path_5m_60 = 5 / np.cos(theta_chi_60)
path_1m_70 = 1 / np.cos(theta_chi_70)
path_2m_70 = 2 / np.cos(theta_chi_70)
path_5m_70 = 5 / np.cos(theta_chi_70)
print("   For a wavelength of 0.48 um with n=1.336 and theta_0 = 15°, path length in water at 1 m depth = " + str(path_1m_48) + " m")
print("   For a wavelength of 0.48 um with n=1.336 and theta_0 = 15°, path length in water at 2 m depth = " + str(path_2m_48) + " m")
print("   For a wavelength of 0.48 um with n=1.336 and theta_0 = 15°, path length in water at 5 m depth = " + str(path_5m_48) + " m")
print("   For a wavelength of 0.60 um with n=1.333 and theta_0 = 15°, path length in water at 1 m depth = " + str(path_1m_60) + " m")
print("   For a wavelength of 0.60 um with n=1.333 and theta_0 = 15°, path length in water at 2 m depth = " + str(path_2m_60) + " m")
print("   For a wavelength of 0.60 um with n=1.333 and theta_0 = 15°, path length in water at 5 m depth = " + str(path_5m_60) + " m")
print("   For a wavelength of 0.70 um with n=1.330 and theta_0 = 15°, path length in water at 1 m depth = " + str(path_1m_70) + " m")
print("   For a wavelength of 0.70 um with n=1.330 and theta_0 = 15°, path length in water at 2 m depth = " + str(path_2m_70) + " m")
print("   For a wavelength of 0.70 um with n=1.330 and theta_0 = 15°, path length in water at 5 m depth = " + str(path_5m_70) + " m")
print("")
ref_prl_48 = refr.getParallelReflFresnel(1.0, 1.336, 9.33e-10, 0.0, refr.radFromDeg(15))
ref_ppd_48 = refr.getPerpendicularReflFresnel(1.0, 1.336, 9.33e-10, 0.0, refr.radFromDeg(15))
ref_avg_48 = (ref_prl_48 + ref_ppd_48) / 2
print("   For a wavelength of 0.48 um, the parallel reflectance is:       " + str(ref_prl_48))
print("   For a wavelength of 0.48 um, the perpendicular reflectance is:  " + str(ref_ppd_48))
print("   So, at this wavelength, the average reflectance is              " + str(ref_avg_48))
print("")
ref_prl_60 = refr.getParallelReflFresnel(1.0, 1.333, 1.17e-8, 0.0, refr.radFromDeg(15))
ref_ppd_60 = refr.getPerpendicularReflFresnel(1.0, 1.333, 1.17e-8, 0.0, refr.radFromDeg(15))
ref_avg_60 = (ref_prl_60 + ref_ppd_60) / 2
print("   For a wavelength of 0.48 um, the parallel reflectance is:       " + str(ref_prl_60))
print("   For a wavelength of 0.48 um, the perpendicular reflectance is:  " + str(ref_ppd_60))
print("   So, at this wavelength, the average reflectance is              " + str(ref_avg_60))
print("")
ref_prl_70 = refr.getParallelReflFresnel(1.0, 1.330, 3.62e-8, 0.0, refr.radFromDeg(15))
ref_ppd_70 = refr.getPerpendicularReflFresnel(1.0, 1.330, 3.62e-8, 0.0, refr.radFromDeg(15))
ref_avg_70 = (ref_prl_70 + ref_ppd_70) / 2
print("   For a wavelength of 0.48 um, the parallel reflectance is:       " + str(ref_prl_70))
print("   For a wavelength of 0.48 um, the perpendicular reflectance is:  " + str(ref_ppd_70))
print("   So, at this wavelength, the average reflectance is              " + str(ref_avg_70))
print("")
light_frac_1m_48 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_48) * np.exp(-path_1m_48/e_fold_dist_48)
light_frac_2m_48 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_48) * np.exp(-path_2m_48/e_fold_dist_48)
light_frac_5m_48 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_48) * np.exp(-path_5m_48/e_fold_dist_48)
light_frac_1m_60 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_60) * np.exp(-path_1m_60/e_fold_dist_60)
light_frac_2m_60 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_60) * np.exp(-path_2m_60/e_fold_dist_60)
light_frac_5m_60 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_60) * np.exp(-path_5m_60/e_fold_dist_60)
light_frac_1m_70 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_70) * np.exp(-path_1m_70/e_fold_dist_70)
light_frac_2m_70 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_70) * np.exp(-path_2m_70/e_fold_dist_70)
light_frac_5m_70 = np.cos(refr.radFromDeg(15)) * (1-ref_avg_70) * np.exp(-path_5m_70/e_fold_dist_70)
print("   Putting it all together...")
print("          For light at 0.48 um and depth of 1m, fraction of solar irradiance left is " + str(light_frac_1m_48))
print("          For light at 0.48 um and depth of 2m, fraction of solar irradiance left is " + str(light_frac_2m_48))
print("          For light at 0.48 um and depth of 5m, fraction of solar irradiance left is " + str(light_frac_5m_48))
print("          For light at 0.60 um and depth of 1m, fraction of solar irradiance left is " + str(light_frac_1m_60))
print("          For light at 0.60 um and depth of 2m, fraction of solar irradiance left is " + str(light_frac_2m_60))
print("          For light at 0.60 um and depth of 5m, fraction of solar irradiance left is " + str(light_frac_5m_60))
print("          For light at 0.70 um and depth of 1m, fraction of solar irradiance left is " + str(light_frac_1m_70))
print("          For light at 0.70 um and depth of 2m, fraction of solar irradiance left is " + str(light_frac_2m_70))
print("          For light at 0.70 um and depth of 5m, fraction of solar irradiance left is " + str(light_frac_5m_70))
print("")
print("   Now, to get the light making it back to the surface...")
print("    First, the light from the second reflection event:")
ref_up_prl_48 = refr.getParallelReflFresnel(1.336, 1.0, 9.33e-10, 0.0, 0.0)
ref_up_ppd_48 = refr.getPerpendicularReflFresnel(1.336, 1.0, 9.33e-10, 0.0, 0.0)
ref_up_avg_48 = (ref_up_prl_48 + ref_up_ppd_48) / 2
ref_up_prl_60 = refr.getParallelReflFresnel(1.333, 1.0, 1.17e-8, 0.0, 0.0)
ref_up_ppd_60 = refr.getPerpendicularReflFresnel(1.333, 1.0, 1.17e-8, 0.0, 0.0)
ref_up_avg_60 = (ref_up_prl_60 + ref_up_ppd_60) / 2
ref_up_prl_70 = refr.getParallelReflFresnel(1.330, 1.0, 3.62e-8, 0.0, 0.0)
ref_up_ppd_70 = refr.getPerpendicularReflFresnel(1.330, 1.0, 3.62e-8, 0.0, 0.0)
ref_up_avg_70 = (ref_up_prl_70 + ref_up_ppd_70) / 2
print("      Reflection of up-bound light at 0.48 um is " + str(ref_up_avg_48))
print("      Reflection of up-bound light at 0.60 um is " + str(ref_up_avg_60))
print("      Reflection of up-bound light at 0.70 um is " + str(ref_up_avg_70))
print("      For 0.48 um and 1m depth: " + str(np.round(light_frac_1m_48*0.5*np.exp(-1/e_fold_dist_48) * (1-ref_up_avg_48) / 0.5 * 255,4)) + " E_sun")
print("      For 0.48 um and 1m depth: " + str(np.round(light_frac_1m_48*0.5*np.exp(-2/e_fold_dist_48) * (1-ref_up_avg_48) / 0.5 * 255,4)) + " E_sun")
print("      For 0.48 um and 1m depth: " + str(np.round(light_frac_1m_48*0.5*np.exp(-5/e_fold_dist_48) * (1-ref_up_avg_48) / 0.5 * 255,4)) + " E_sun")
print("      For 0.60 um and 1m depth: " + str(np.round(light_frac_1m_60*0.5*np.exp(-1/e_fold_dist_60) * (1-ref_up_avg_60) / 0.5 * 255,4)) + " E_sun")
print("      For 0.60 um and 1m depth: " + str(np.round(light_frac_1m_60*0.5*np.exp(-2/e_fold_dist_60) * (1-ref_up_avg_60) / 0.5 * 255,4)) + " E_sun")
print("      For 0.60 um and 1m depth: " + str(np.round(light_frac_1m_60*0.5*np.exp(-5/e_fold_dist_60) * (1-ref_up_avg_60) / 0.5 * 255,4)) + " E_sun")
print("      For 0.70 um and 1m depth: " + str(np.round(light_frac_1m_70*0.5*np.exp(-1/e_fold_dist_70) * (1-ref_up_avg_70) / 0.5 * 255,4)) + " E_sun")
print("      For 0.70 um and 1m depth: " + str(np.round(light_frac_1m_70*0.5*np.exp(-2/e_fold_dist_70) * (1-ref_up_avg_70) / 0.5 * 255,4)) + " E_sun")
print("      For 0.70 um and 1m depth: " + str(np.round(light_frac_1m_70*0.5*np.exp(-5/e_fold_dist_70) * (1-ref_up_avg_70) / 0.5 * 255,4)) + " E_sun")


print("")
print("")
print("Question 5.4")
print(" Brewster Angles: ")
brewster_050 = refr.getBrewsterAngle(1.336)
brewster_080 = refr.getBrewsterAngle(1.331)
brewster_165 = refr.getBrewsterAngle(1.316)
print("   For 0.5 um:  " + str(refr.degFromRad(brewster_050)) + "°")
print("   For 0.8 um:  " + str(refr.degFromRad(brewster_080)) + "°")
print("   For 1.65 um: " + str(refr.degFromRad(brewster_165)) + "°")
print(" Angles of Refraction: ")
theta_chi_050 = refr.getRefractionAngle(1.0, 1.336, brewster_050)
theta_chi_080 = refr.getRefractionAngle(1.0, 1.331, brewster_080)
theta_chi_165 = refr.getRefractionAngle(1.0, 1.316, brewster_165)
print("   For 0.5 um:  " + str(refr.degFromRad(theta_chi_050)) + "°")
print("   For 0.8 um:  " + str(refr.degFromRad(theta_chi_080)) + "°")
print("   For 1.65 um: " + str(refr.degFromRad(theta_chi_165)) + "°")
print("")
print(" Perpendicular Reflectance of water: ")
refl_ppd_050 = refr.getPerpendicularReflFresnel(1.0, 1.336, 0.0, 1.02e-9, brewster_050)
refl_ppd_080 = refr.getPerpendicularReflFresnel(1.0, 1.331, 0.0, 1.29e-7, brewster_080)
refl_ppd_165 = refr.getPerpendicularReflFresnel(1.0, 1.316, 0.0, 7.75e-5, brewster_165)
print("   at 0.50 um: " + str(refl_ppd_050))
print("   at 0.80 um: " + str(refl_ppd_080))
print("   at 1.65 um: " + str(refl_ppd_165))
print(" Overall Reflectance of water: ")
refl_050 = (refr.getParallelReflFresnel(1.0, 1.336, 0.0, 1.02e-9, brewster_050) + refl_ppd_050) / 2
refl_080 = (refr.getParallelReflFresnel(1.0, 1.331, 0.0, 1.29e-7, brewster_080) + refl_ppd_080) / 2
refl_165 = (refr.getParallelReflFresnel(1.0, 1.316, 0.0, 7.75e-5, brewster_165) + refl_ppd_165) / 2
print("   at 0.50 um: " + str(refl_050))
print("   at 0.80 um: " + str(refl_080))
print("   at 1.65 um: " + str(refl_165))




print("")
print("")
print("Question 5.5")
print("  Irradiance at the water:")
irradiance_5 = 1848.0243695642423 * np.cos(refr.radFromDeg(20))
irradiance_6 = 1713.444655900252 * np.cos(refr.radFromDeg(20))
irradiance_9 = 940.6471903181829 * np.cos(refr.radFromDeg(20))
print("    Irradiance at the water's surface at 0.5 um: " + str(irradiance_5) + " W/m^2/sr")
print("    Irradiance at the water's surface at 0.5 um: " + str(irradiance_6) + " W/m^2/sr")
print("    Irradiance at the water's surface at 0.5 um: " + str(irradiance_9) + " W/m^2/sr")
print("  Refraction Angle:")
theta_chi_5 = refr.getRefractionAngle(1.0, 1.336, refr.radFromDeg(20))
theta_chi_6 = refr.getRefractionAngle(1.0, 1.333, refr.radFromDeg(20))
theta_chi_9 = refr.getRefractionAngle(1.0, 1.329, refr.radFromDeg(20))
print("    Refraction angle at 0.5 um: " + str(refr.degFromRad(theta_chi_5)) + "°")
print("    Refraction angle at 0.6 um: " + str(refr.degFromRad(theta_chi_6)) + "°")
print("    Refraction angle at 0.9 um: " + str(refr.degFromRad(theta_chi_9)) + "°")
print("  Reflection:")
total_refl_5 = (refr.getPerpendicularReflFresnel(1.0, 1.336, 0, 1.02e-9, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
total_refl_6 = (refr.getPerpendicularReflFresnel(1.0, 1.333, 0, 1.17e-8, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
total_refl_9 = (refr.getPerpendicularReflFresnel(1.0, 1.329, 0, 4.81e-7, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
print("    Reflection at 0.5 um: " + str(total_refl_5))
print("    Reflection at 0.5 um: " + str(total_refl_6))
print("    Reflection at 0.5 um: " + str(total_refl_9))
print("  Next, the absorptivity of water at each wavelength:")
alpha_water_5 = refr.getAlphaFromK(1.02e-9, 0.5e-6)
alpha_water_6 = refr.getAlphaFromK(1.17e-8, 0.6e-6)
alpha_water_9 = refr.getAlphaFromK(4.81e-7, 0.9e-6)
print("    Absorption Coefficient at 0.5 um: " + str(alpha_water_5))
print("    Absorption Coefficient at 0.6 um: " + str(alpha_water_6))
print("    Absorption Coefficient at 0.9 um: " + str(alpha_water_9))
print("  Reflection at surface for upwelling radiation: ")
total_refl_up_5 = (refr.getPerpendicularReflFresnel(1.336, 1.0, 1.02e-9, 0, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
total_refl_up_6 = (refr.getPerpendicularReflFresnel(1.333, 1.0, 1.17e-8, 0, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
total_refl_up_9 = (refr.getPerpendicularReflFresnel(1.329, 1.0, 4.81e-7, 0, refr.radFromDeg(20)) + refr.getParallelReflFresnel(1.0, 1.336, 0, 4.81e-7, refr.radFromDeg(20))) / 2
print("    Reflection of upwelling light at the surface, at 0.5 um: " + str(total_refl_up_5))
print("    Reflection of upwelling light at the surface, at 0.6 um: " + str(total_refl_up_6))
print("    Reflection of upwelling light at the surface, at 0.9 um: " + str(total_refl_up_9))
print("  Now, putting all the coefficients together into a coherent equation...")
#   L = A * exp(B * depth)
A_5 = 1/np.pi * irradiance_5 * (1-total_refl_5) * (1-total_refl_up_5) * 0.25
B_5 = - alpha_water_5 * (1.0 + 1.0/np.cos(total_refl_5))
A_6 = 1/np.pi * irradiance_6 * (1-total_refl_6) * (1-total_refl_up_6) * 0.25
B_6 = - alpha_water_6 * (1.0 + 1.0/np.cos(total_refl_6))
A_9 = 1/np.pi * irradiance_9 * (1-total_refl_9) * (1-total_refl_up_9) * 0.25
B_9 = - alpha_water_9 * (1.0 + 1.0/np.cos(total_refl_9))
print("    For 0.5 um light, A = " + str(A_5) + " and B = " + str(B_5) + " and A*B is " + str(A_5*B_5))
print("    For 0.6 um light, A = " + str(A_6) + " and B = " + str(B_6) + " and A*B is " + str(A_6*B_6))
print("    For 0.9 um light, A = " + str(A_9) + " and B = " + str(B_9) + " and A*B is " + str(A_9*B_9))
print("  Now, finally, plugging in to get the rate of change in radiance in each wavelength at each depth:")
change_rate_5_p1 = - A_5 * B_5 * np.exp(B_5 * 0.1)
change_rate_5_2 = - A_5 * B_5 * np.exp(B_5 * 2.0)
change_rate_5_10 = - A_5 * B_5 * np.exp(B_5 * 10.0)
change_rate_6_p1 = - A_6 * B_6 * np.exp(B_6 * 0.1)
change_rate_6_2 = - A_6 * B_6 * np.exp(B_6 * 2.0)
change_rate_6_10 = - A_6 * B_6 * np.exp(B_6 * 10.0)
change_rate_9_p1 = - A_9 * B_9 * np.exp(B_9 * 0.1)
change_rate_9_2 = - A_9 * B_9 * np.exp(B_9 * 2.0)
change_rate_9_10 = - A_9 * B_9 * np.exp(B_9 * 10.0)
print("    Radiance rate of change in 0.5 um at 0.1 m depth: " + str(change_rate_5_p1) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.6 um at 0.1 m depth: " + str(change_rate_6_p1) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.9 um at 0.1 m depth: " + str(change_rate_9_p1) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.5 um at 2.0 m depth: " + str(change_rate_5_2) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.6 um at 2.0 m depth: " + str(change_rate_6_2) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.9 um at 2.0 m depth: " + str(change_rate_9_2) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.5 um at 10.0 m depth: " + str(change_rate_5_10) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.6 um at 10.0 m depth: " + str(change_rate_6_10) + str(" W/m^2/um/sr"))
print("    Radiance rate of change in 0.9 um at 10.0 m depth: " + str(change_rate_9_10) + str(" W/m^2/um/sr"))
print("  Finally, to esetimate the depth at which the sensor is no longer picking up anything...")
max_depth = np.log(11.0 / A_5) / B_5
print("    Lowest measureable depth: " + str(max_depth) + "m")

depths = np.linspace(0, 10, 100)
radiance_5 = A_5 * B_5 * np.exp(B_5 * depths)
radiance_6 = A_6 * B_6 * np.exp(B_6 * depths)
radiance_9 = A_9 * B_9 * np.exp(B_9 * depths)

# Set up plot, add lines
fig, ax = plt.subplots(1,1)
ax.plot(depths, np.log(-radiance_5), 'g-')
ax.plot(depths, np.log(-radiance_6), 'r-')
ax.plot(depths, np.log(-radiance_9), 'k-')
# Captions and Axis labels
plt.xlabel("Depth (m)")
plt.ylabel("Log of Negative Rate of Change in Radiance log(W/m^2/sr/um/m)")
# Set axis tick marks and grid parameters
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(1/5))
plt.grid(color="gray", linestyle="--")

fig.tight_layout(pad=1)

#   Print plot
plt.savefig("radiance_with_depth.png")






# Midterm
print("")
print("")
print("************************")
print("Midterm!")
total_refl_0p6 = (refr.getPerpendicularReflFresnel(1.0, 1.4585, 0.0, refr.getKFromAlpha(0.6285e2,0.6e-6), 0.0) + refr.getParallelReflFresnel(1.0, 1.4585, 0.0, refr.getKFromAlpha(0.6285e2,0.6e-6), 0.0)) / 2
total_refl_0p6_second = (refr.getPerpendicularReflFresnel(1.4585, 1.0, refr.getKFromAlpha(0.6285e2,0.6e-6), 0.0, 0.0) + refr.getParallelReflFresnel(1.4585, 1.0, refr.getKFromAlpha(0.6285e2,0.6e-6), 0.0, 0.0)) / 2
total_refl_10p = (refr.getPerpendicularReflFresnel(1.0, 1.65, 0.0, refr.getKFromAlpha(140.67e2,10.0e-6), 0.0) + refr.getParallelReflFresnel(1.0, 1.65, 0.0, refr.getKFromAlpha(140.67e2,10.0e-6), 0.0)) / 2
total_refl_10p_second = (refr.getPerpendicularReflFresnel(1.65, 1.0, refr.getKFromAlpha(140.67e2,10.0e-6), 0.0, 0.0) + refr.getParallelReflFresnel(1.65, 1.0, refr.getKFromAlpha(140.67e2,10.0e-6), 0.0, 0.0)) / 2
print("  Reflection factor for glass for 0.6 um light:    " + str(total_refl_0p6))
print("  Reflection factor for glass for 0.6 um light #2: " + str(total_refl_0p6_second))
print("  Reflection factor for glass for 0.6 um light:    " + str(total_refl_10p))
print("  Reflection factor for glass for 0.6 um light #2: " + str(total_refl_10p_second))
print("  Absorption in glass at 0.6 um: " + str(1 - np.exp(-0.6285*0.2)))
print("  Absorption in glass at 10. um: " + str(1 - np.exp(-140.67*0.2)))


#refr.getPerpendicularReflFresnel(n_1, n_2, k_1, k_2, theta_0):




#
