#!/usr/bin/env python

CellX = 200.0
CellY = 300.0
CellZ = 200.0
wWire = 5.0
lSplit = 200.0
wSplit = 20.0
lGap = 150.0
lEllipsoid = 150.0

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

 
