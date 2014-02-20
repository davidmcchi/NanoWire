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
Cyl3.height = lGap

#cylinder2
Cyl2 = cylinder()
Cyl2.center = 
Cyl2.axis = [x-y for x,y zip(Cyl1.center,Cyl3.center)] #Move centers to end of cylinder 1 and 3


radius of connectors is same. same as radius of wire







#topwirecoordinates
lWire = (CellY - lSplit)*0.5
topwirecenter = [0,(lSplit+ lWire)/2.0,0]
hWire = wWire
topwiresize = [wWire,lWire,hWire]

#bottomwirecoordinates
bottomwirecenter = [topwirecenter[0],-1*topwirecenter[1],topwirecenter[2]]
bottomwiresize = topwiresize

#topconecoordinates
topconeheight = (lSplit-lGap)*0.5
topconecenter = [0, 0.5*(lGap+topconeheight),0]
topconetopradius = wWire/2
topconebottomradius = wSplit/2
axis = [0,1,0]

#bottomconecoordinates
bottomconeheight = topconeheight
bottomconecenter = [topconecenter[0],-1*topconecenter[1],topconecenter[0]]
bottomconetopradius = topconetopradius
bottomconebottomradius = topconebottomradius
axis = [0,-1,0]

#center cylinder coordinates
radius = wSplit*0.5 
height = lWire
axis = [0,1,0]

#ellipsoidcoordinates
ellipsoidcenter = [0,0,0]
ellipsoidsize = [(wSplit-2*wWire),lEllipsoid,(hSplit-2*wWire)]



 
