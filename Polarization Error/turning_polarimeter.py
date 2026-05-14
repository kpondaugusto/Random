#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('turning_polarimeter_KRP_south_arm.csv',  skiprows=8)
# %%
df_smaller_angle = pd.read_csv('turning_polarimeter_KRP_south_arm_smaller.csv',  skiprows=8)
# %%
dolp = df[' DOLP[%] ']
docp = df[' DOCP[%] ']
azimuth = df[' Azimuth[°] ']
azimuths = np.array(azimuth)
ellipticity = df[' Ellipticity[°] ']
ellipticities = np.array(ellipticity)
power = df[' Pol Power[mW] ']
Power = np.array(power)
power_scaled = 20 + 180 * (Power - Power.min()) / (Power.max() - Power.min())

azimuth_s = df_smaller_angle[' Azimuth[°] ']
ellipticity_s = df_smaller_angle[' Ellipticity[°] ']
# %%
# fig, ax = plt.subplots(1,2)

# ax[0].plot(np.abs(azimuth), ellipticity, linestyle='',marker='.')
# ax[1].plot(np.abs(azimuth_s),ellipticity_s,linestyle='',marker='.')
# %%
# 2. Convert degrees to radians for trigonometric functions
psi = np.radians(azimuths)
chi = np.radians(ellipticities)

# 3. Calculate Stokes Cartesian coordinates on the unit sphere
S1 = np.cos(2 * chi) * np.cos(2 * psi)
S2 = np.cos(2 * chi) * np.sin(2 * psi)
S3 = np.sin(2 * chi)
#%%
# 4. Create 3D Figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 5. Generate Reference Background Wireframe Sphere
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
sphere_x = np.cos(u) * np.sin(v)
sphere_y = np.sin(u) * np.sin(v)
sphere_z = np.cos(v)
ax.plot_surface(sphere_x, sphere_y, sphere_z, color='gray', alpha=0.1, linewidth=0.5, edgecolors='lightgray')

# 6. Plot Reference Axes Lines
ax.plot([-1, 1], [0, 0], [0, 0], color='black', linestyle='--', alpha=0.5)
ax.plot([0, 0], [-1, 1], [0, 0], color='black', linestyle='--', alpha=0.5)
ax.plot([0, 0], [0, 0], [-1, 1], color='black', linestyle='--', alpha=0.5)

# 7. Plot Your Data Trajectory
# Line connects sequential points; scatter colors points chronologically
ax.plot(S1, S2, S3, color='blue', alpha=0.7, label='Polarization Path')
sc = ax.scatter(S1, S2, S3, c=range(len(S1)), cmap='viridis', s=30, depthshade=False)

# 8. Visual Adjustments
ax.set_xlabel('S1 (Linear H/V)')
ax.set_ylabel('S2 (Linear ±45°)')
ax.set_zlabel('S3 (Circular L/R)')
ax.set_title('Data Trajectory on Poincaré Sphere')

# Force equal axis aspect ratio
ax.set_box_aspect([1,1,1]) 

# Add sequence progress colorbar
cbar = fig.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Data Point Index (Time/Sequence)')

plt.legend()
plt.show()
 #%%
# 3. Setup Figure
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')

# 4. Generate local reference wireframe patch near S1 = -1
u, v = np.mgrid[-0.1*np.pi:0.2*np.pi:30j, 0.4*np.pi:0.6*np.pi:30j]
sphere_x = -np.cos(u) * np.sin(v)  # Shifted to negative S1 face
sphere_y = np.sin(u) * np.sin(v)
sphere_z = np.cos(v)
ax.plot_surface(sphere_x, sphere_y, sphere_z, color='gray', alpha=0.05, linewidth=0.3, edgecolors='lightgray')

# 5. Plot the Path and Points
ax.plot(S1, S2, S3, color='blue', alpha=0.7, linewidth=1.5, label='Polarization Track')
sc = ax.scatter(S1, S2, S3, c=range(len(S1)), 
                cmap='jet', s=power_scaled,
                edgecolors='black', linewidths=0.5,
                 label='Points (Size=Power)')

# 6. Dynamic Limits: Crop window tightly based on data extrema + margin padding
pad = 0.03
ax.set_xlim([S1.min() - pad, S1.max() + pad])
ax.set_ylim([S2.min() - pad, S2.max() + pad])
ax.set_zlim([S3.min() - pad, S3.max() + pad])

# 7. Labels and Formatting
ax.set_xlabel('S1 (Linear H/V)')
ax.set_ylabel('S2 (Linear ±45°)')
ax.set_zlabel('S3 (Circular L/R)')
ax.set_title('Zoomed In View (Negative S1 Face - Vertical Linear)', pad=15)
ax.set_box_aspect((1, 1, 1))

# Add step tracking sidebar
cbar = fig.colorbar(sc, ax=ax, shrink=0.5, aspect=12)
cbar.set_label('Sequence Index (Color) | Power (Marker Size)')

plt.legend(loc='upper left')
ax.view_init(elev=0, azim=180)
plt.show()
# %%
