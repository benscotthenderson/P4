#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:58:01 2024

@author: benhenderson
"""

import xarray as xr 
import matplotlib.pyplot as plt  
import numpy as np 

# Read in the NetCDF dataset containing chlorophyll data
data = xr.open_dataset('ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')

# Extracing a subset of data within specific extents
data_extents = data.sel(lat=slice(-5, -7.25), lon=slice(-83, -81))

# Defining variables latitude and longitude and calculating the mean chlorophyll concentration
latitude = data_extents['lat']
longitude = data_extents['lon']
ma_chlor = data_extents['chlor_a'].mean(dim='time')

# Create a figure and axes for plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting filled contours of mean chlorophyll concentration
contour = ax.contourf(longitude, latitude, ma_chlor, levels=np.linspace(0, 7, 200), cmap='turbo')

# Adding a colorbar to the plot and formatting the colorbar ticks
plt.colorbar(contour, label='Chlorophyll Concentration (mg/m³)', ticks=np.arange(0, 7, 1))

# Formatting the plot title and axis labels
plt.title('Mean Annual Chlorophyll', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
