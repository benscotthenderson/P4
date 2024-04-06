#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:22:22 2024

@author: benhenderson
"""

import xarray as xr 
import matplotlib.pyplot as plt  
import numpy as np  
import cartopy.crs as ccrs  

# Reading in the NetCDF dataset containing bathymetric data
data = xr.open_dataset('GMRT_humboldt.nc')

# Extracting latitude, longitude, and bathymetry data from the dataset
latitude = data['lat']
longitude = data['lon']
bathymetry = data['altitude']

# Masking land regions where altitude is > 0
bathymetry_no_land = np.ma.masked_where(bathymetry >= 0, bathymetry)

# Creating a figure and axes for plotting and setting the CRS of the data
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection':ccrs.PlateCarree()})

# Plotting filled contours of bathymetric data and creating 500 levels between -6000 and 0
contour = ax.contourf(longitude, latitude, bathymetry_no_land, levels=np.linspace(-6000, 0, 500), transform=ccrs.PlateCarree(), cmap='jet')

# Adding a colorbar to the plot and formatting the colorbar ticks
plt.colorbar(contour, label='Depth (m)', ticks=np.arange(-6000, 0, 500))

# Adding coastlines to the plot
ax.coastlines(resolution='10m')

# Adding gridlines to the plot
gl = ax.gridlines(draw_labels=True)
gl.right_labels = False
gl.top_labels = False

# Adding the plot title
plt.title('Bathymetry Map of Humboldt Current', fontsize=16)

