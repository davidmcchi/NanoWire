#!/usr/bin/env python
import numpy as np

class cylinder():
	self.axis = np.array([0.0,1.0,0.0])
	self.height = 1.0
	self.radius = 1.0
	self.material = "Ag"
	self.center = np.array([0.0,0.0,0.0])

class sphere():
	self.center = np.array([0.0,0.0,0.0])
	self.material = "Ag"
	self.radius = 1.0

class block():
	self.size = np.array([1.0,1.0,1.0])
	self.material = "Ag"
	self.center = np.array([0.0,0.0,0.0])

#Base Parameters, 1.0 unit = 100.0 nm
CellX = 200.0
CellY = 300.0
CellZ = 200.0
rWire = 2.5 	#Let's use the radius instead of the diameter, it's a more natural choice
lSplit = 200.0
wSplit = 20.0
lGap = 150.0
tSlab = 10.0	#thickness of the silver slab base

#Derived Parameters
lWire = (CellY - lSplit)*0.5

#cylinder1
Cyl1= cylinder()
Cyl1.center = [0,((lSplit+lWire)/2,0]
Cyl1.height = (CellX-lSplit)/2

#cylinder3
Cyl3 = cylinder()
Cly3.center = [.5wSplit+wWire,0,0]
Cyl3.height = lGap

#cylinder2
Cyl2 = cylinder()
Cyl2.center = [(.5wSplit+wWire)/2,.5((lSplit+lwWire)/2)
Cly2.height = lGap
Cyl2.axis = [x-y for x,y zip(Cyl1.center,Cyl3.center)] 
#Move centers to end of cylinder 1 and 3

#sphereA
SphA = sphere()
SphA.center = [0,lSplit/2,0]
SphA.radius = .5wWire

#sphereB
SphB = sphere()
SphB.center = [.5wSplit+wWire,.5lSplit,0]
SphB.radius = SphA.radius

radius of connectors is same. same as radius of wire

