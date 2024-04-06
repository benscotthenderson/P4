#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:58:01 2024

@author: benhenderson
"""

import xarray as xr
import numpy as np  

# Read in the NetCDF dataset containing chlorophyll data extract a subset of data within specific extents
data = xr.open_dataset('ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')

# Extracting a subset of data within specific extents
data_extents = data.sel(lat=slice(-5, -7.25), lon=slice(-83, -81))

# Calculating the monthly mean chlorophyll concentration
monthly_mean = data_extents.groupby('time.month').mean()

# Defining month names
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Assigning month names to months in the dataset
monthly_mean['month'] = months

# Plotting monthly mean chlorophyll concentration for each month
monthly_mean.chlor_a.plot(col='month', col_wrap=4, cmap='turbo', levels=np.linspace(0, 7, 100), cbar_kwargs={'label':'Chlorophyll Concentration (mg/m³)'})

