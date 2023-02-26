#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 13:10:27 2018

@author: andrewpauling
"""

import numpy as np
import xarray as xr
import scipy.interpolate as interp


def fixmonth(dfile):

    """Fix CESM months since by default the timestamp is for the first day of
    the next month

    Parameters
    ----------

    dfile : xarray dataset
            Dataset containing time to fix

    Returns
    -------

    dfile : xarray dataset
            Fixed dataset
    """

    mytime = dfile['time'][:].data
    for time in range(mytime.size):
        if mytime[time].month > 1:
            mytime[time] = mytime[time].replace(month=mytime[time].month-1)
        elif mytime[time].month == 1:
            mytime[time] = mytime[time].replace(month=12)
            mytime[time] = mytime[time].replace(year=mytime[time].year-1)

    dfile = dfile.assign_coords(time=mytime)

    return dfile


def globalmean(da):
    return da.weighted(np.cos(np.deg2rad(da.lat))).mean(("lat", "lon"))
