#!/usr/bin/env python

class cylinder():
        axis = [0,1,0]
        height = 1.0
        radius = 1.0
        material = "Ag"
        center = [0,0,0]

class sphere():
        center = [0,0,0]
        material = "Ag"
        radius = 1.0

CellX = 200.0
CellY = 300.0
CellZ = 200.0
wWire = 5.0
lSplit = 200.0
wSplit = 20.0
lGap = 150.0
lEllipsoid = 150.0
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

