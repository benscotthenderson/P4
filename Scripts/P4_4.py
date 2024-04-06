#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:41:51 2024

@author: benhenderson
"""

import xarray as xr  
import matplotlib.pyplot as plt  
import numpy as np  
 
# Read in the NetCDF dataset containing chlorophyll data
data = xr.open_dataset('ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')

# Extract a subset of data within specific extents
data_extents = data.sel(lat=slice(-5, -7.25), lon=slice(-83, -81))

# Extracting latitude, longitude, and chlorophyll data within the specified extents
latitude = data_extents['lat']
longitude = data_extents['lon']
chlor = data_extents['chlor_a']

# Calculating mean chlorophyll concentration for each month over the specified region
chlor_region_season = chlor.groupby('time.month').mean(dim=['lat', 'lon', 'time'])

# Creating a plot for mean chlorophyll concentration at a single grid point and the mean seasonal cycle
axis = plt.axes()
chlor.sel(lat=-5.35, lon=-81.2, method='nearest').groupby('time.month').mean().plot(ax=axis, label='Single Grid Point (5.35ᴼS, 81.20ᴼW)', marker='o')
chlor_region_season.plot(ax=axis, label='Mean Seasonal Cycle', marker='o')

# Set the x-axis ticks and labels
plt.xticks(np.arange(1, 13, 1), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Set labels for the x-axis and y-axis
plt.xlabel('Months')
plt.ylabel('Chlorophyll Concentration (mg/m³)')

# Add a legend to the plot
plt.legend()



