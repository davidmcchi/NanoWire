#!/usr/bin/env python

import sys, os, h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Check if a directory name has been provided
if len(sys.argv) < 2:
        sys.exit('Usage: Provide the name of an hdf5 file')
H5dpwrFile = sys.argv[1]
print("Getting data from %s" % H5dpwrFile)

# Load the field data file into a python object
H5dpwrFullData = h5py.File(H5dpwrFile,'r')

# Extract only the desired data set, assuming this is a dpwr file
dpwrData = H5dpwrFullData['/denergy']

# generate two arrays, x and y, specifying the coordinate locations
y,x = np.mgrid[0:dpwrData.shape[0]+1,0:dpwrData.shape[1]+1]

# specify which time slice you want
# time should be >= 0 or and < maxTime
# time = -1 extracts the last time slice and is equivalent to maxTime-1
maxTime = len(dpwrData[0][0])
time = -1

# finally, get just the intensity data into a 2D array
fieldPower = dpwrData[:][:][time]

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
fieldPower = fieldPower[:-1, :-1]

# I'll show you how to plot the data later, but for now, everything you need is in x,y, and fieldPower
# Your code for finding the local maxima should go here
# Google things if you get stuck, such as "how to find maximum values of a 2D data set"
# Otherwise, let's plan on meeting Friday
