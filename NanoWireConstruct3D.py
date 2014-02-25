#!/usr/bin/env python
import numpy as np

class cylinder():
	def __init__(self):
		self.axis = np.array([0.0,1.0,0.0])
		self.height = 1.0
		self.radius = 1.0
		self.material = "Ag"
		self.center = np.array([0.0,0.0,0.0])

	def summary(self):
		objype = "type\tcylinder"
		cent = "center\t%s" % ",".join([str(x) for x in self.center])
		rad = "radius\t%f" % self.radius
		hght = "height\t%f" % self.height
		mat = "material\t%s" % self.material
		ax = "axis\t%s" % ",".join([str(x) for x in self.axis])
		return [objype,cent,rad,hght,ax,mat]

class sphere():
	def __init__(self):
		self.center = np.array([0.0,0.0,0.0])
		self.material = "Ag"
		self.radius = 1.0

	def summary(self):
		objype = "type\tsphere"
		cent = "center\t%s" % ",".join([str(x) for x in self.center])
		rad = "radius\t%f" % self.radius
		mat = "material\t%s" % self.material
		return [objype,cent,rad,mat]

class block():
	def __init__(self):
		self.size = np.array([1.0,1.0,1.0])
		self.material = "Ag"
		self.center = np.array([0.0,0.0,0.0])	

	def summary(self):
		objype = "type\tblock"
		cent = "center\t%s" % ",".join([str(x) for x in self.center])
		sz = "size\t%s" % ",".join([str(x) for x in self.size])
		mat = "material\t%s" % self.material
		return [objype,cent,sz,mat]

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
Cyl1 = cylinder()
Cyl1.center = np.array([0,(lSplit+lWire)/2.0,0.0])
Cyl1.axis = np.array([0.0, 1.0, 0.0])
Cyl1.height = lWire
Cyl1.radius = rWire

#cylinder3
Cyl3 = cylinder()
Cyl3.center = np.array([-0.5*wSplit-rWire,0.0,0.0])
Cyl3.axis = Cyl1.axis
Cyl3.height = lGap
Cyl3.radius = rWire

#sphereA
SphA = sphere()
SphA.center = Cyl1.center - np.array([0.0,lSplit/2.0,0.0])
SphA.radius = rWire

#sphereB
SphB = sphere()
SphB.center = Cyl3.center + np.array([0.0,lGap/2.0,0.0])
SphB.radius = SphA.radius

#cylinder2
Cyl2 = cylinder()
Cyl2.center = 0.5*(SphA.center + SphB.center)
Cyl2.axis = (SphA.center - SphB.center)
Cyl2.height = np.linalg.norm(Cyl2.axis)
Cyl2.radius = rWire

#slab
Slab = block()
Slab.center = np.array([0.0,0.0,-0.5*tSlab])
Slab.size = np.array([CellX, CellY, tSlab])

OBJS = [Cyl1,Cyl2,Cyl3,SphA,SphB,Slab]
for num,obj in enumerate(OBJS): 
	print("##OBJ%i" % (num+1))
	print("\n".join(obj.summary()))
	print("##ENDOBJ%i" % (num+1))

