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
CellX = 100.0
CellY = 300.0
CellZ = 100.0
rWire = 2.5 	#Let's use the radius instead of the diameter, it's a more natural choice
lSplit = 200.0
wSplit = 20.0
lGap = 150.0
tSlab = 10.0	#thickness of the silver slab base

#Derived Parameters
lWire = (CellY - lSplit)*0.5

#(+x,+y)
#cylinder1
Cyl1 = cylinder()
Cyl1.center = np.array([0,(lSplit+lWire)/2.0,0.0])
Cyl1.axis = np.array([0.0, 1.0, 0.0])
Cyl1.height = lWire
Cyl1.radius = rWire

#cylinder3
Cyl3 = cylinder()
Cyl3.center = np.array([0.5*wSplit+rWire,0.0,0.0])
Cyl3.axis = Cyl1.axis
Cyl3.height = lGap
Cyl3.radius = rWire

#sphereA
SphA = sphere()
SphA.center = Cyl1.center - np.array([0.0,lWire/2.0,0.0])
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

#(-x,+y)
#cylinder2 reflection over yz plane
Cyl4 = cylinder()
Cyl4.center = np.array([-1.0*Cyl2.center[0],Cyl2.center[1],Cyl2.center[2]])
Cyl4.axis = np.array([-1.0*Cyl2.axis[0],Cyl2.axis[1],Cyl2.axis[2]])
Cyl4.height = Cyl2.height
Cyl4.radius = rWire

#sphereB reflection over yz plane
SphC = sphere()
SphC.center = np.array([-1.0*SphB.center[0],SphB.center[1],SphB.center[2]])
SphC.radius = SphA.radius

#cylinder3 reflection over yz plane
Cyl5 = cylinder()
Cyl5.center = np.array([-1.0*Cyl3.center[0],Cyl3.center[1],Cyl3.center[2]])
Cyl5.axis = Cyl1.axis
Cyl5.height = lGap
Cyl5.radius = rWire

#(+x,-y)
#cylinder1 reflection over xz plane
Cyl6 = cylinder()
Cyl6.center = np.array([0,-1.0*(lSplit+lWire)/2.0,0.0])
Cyl6.axis = np.array([0.0, 1.0, 0.0])
Cyl6.height = lWire
Cyl6.radius = rWire

#sphereA reflection over xz plane
SphD = sphere()
SphD.center = Cyl6.center + np.array([0.0,lWire/2.0,0.0])
SphD.radius = rWire

#sphereB reflection over xz plane
SphE = sphere()
SphE.center = Cyl5.center - np.array([0.0,lGap/2.0,0.0])
SphE.radius = SphA.radius

#cylinder2 reflection over xz plane
Cyl7 = cylinder()
Cyl7.center = 0.5*(SphD.center + SphE.center)
Cyl7.axis = (SphD.center - SphE.center)
Cyl7.height = np.linalg.norm(Cyl2.axis)
Cyl7.radius = rWire

#(-x,-y)
#sphereB reflected through origin
SphF = sphere()
SphF.center = np.array([-1.0*SphB.center[0],-1.0*SphB.center[1],SphB.center[2]])
SphF.radius = SphA.radius

#cylinder2 reflected through origin
Cyl8 = cylinder()
Cyl8.center = 0.5*(SphD.center + SphF.center)
Cyl8.axis = (SphD.center - SphF.center)
Cyl8.height = np.linalg.norm(Cyl2.axis)
Cyl8.radius = rWire

#slab
Slab = block()
Slab.center = np.array([0.0,0.0,-0.5*tSlab])
Slab.size = np.array([CellX, CellY, tSlab])

OBJS = [Cyl1,Cyl2,Cyl3,Cyl4,Cyl5,Cyl6,Cyl7,Cyl8,SphA,SphB,SphC,SphD,SphE,SphF,Slab]
for num,obj in enumerate(OBJS):
	print("##OBJ%i" % (num+1))
	print("\n".join(obj.summary()))
	print("##ENDOBJ%i" % (num+1))

