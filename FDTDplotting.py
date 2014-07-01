import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("!!!filename!!!",usecols=(0))
nx = max(x)+1

#Same for y column

z = np.zeros((nx,ny),dtype=float)
datafile = open("!!!filename!!!","r")
