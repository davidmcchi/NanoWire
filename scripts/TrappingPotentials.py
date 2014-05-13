#!/usr/bin/env python
#Code for running FDTD Calculations using custom input files and the python-meep interface
#Author: Joshua E. Szekely
#November 2013, v 1.0.0
#Updated 12/9/13

import sys,os,shutil
import numpy as np
import matplotlib.pyplot
import random
from scipy.constants import c, epsilon_0, mu_0

#xyz coordinate class
class xyz:
	def __init__(self,xval,yval,zval):
		self.x = xval
		self.y = yval
		self.z = zval

#Filler is placed in empty coordinate positions
def makexyz(chars,filler):
	x = y = z = filler
	crds = chars.split(',')
	if len(crds) is 1:
		x = float(crds[0])
	elif len(crds) is 2:
		x = float(crds[0])
		y = float(crds[1])
	else:
		x = float(crds[0])
		y = float(crds[1])
		z = float(crds[2])
	return xyz(x,y,z)

#****************************************************************
# Read the input file
# Looks for the folowing sections:
#	COMP		Computational Parameters
#	STRUCTURES	Geometric objects with dielectric info
#	BOUNDARY	Boundary conditions for the calculation
#	SOURCE		Info on the light source
#	RUNINFO		Calculation runtime information
#	OUTPUTS		What to output and when
#****************************************************************

print "Parsing the input file..."
inputfile = sys.argv[1]
if not os.path.isfile(inputfile):
	print "Error: The provided file does not exist in the current directory"
	print "File = %s" % inputfile
	print "Current Directory = %s" % os.getcwd()
	exit(-1)

#COMP
#imports the number of dimensions, cell dimensions, meep a value, and resolution
instream = open(inputfile,"r")
importline = False
CompArgs = []
for line in instream:
	if '#ENDCOMP' in line:
		importline = False
	if importline is True:
		CompArgs.append(line)
	if '#COMP' in line:
		importline = True
instream.close()

procs = None
acct = None
for arg in CompArgs:
	modarg = arg.split()
	if 'dimen' in modarg[0]:
		NumDimensions = int(modarg[1])
	if 'cellsize' in modarg[0]:
		CellSize = modarg[1]
		CellSize = makexyz(CellSize,"no-size")
	if 'resolution' in modarg[0]:
		resolution = int(modarg[1])
	if 'fhandle' in modarg[0]:
		fhandle = modarg[1]
	else:
		fhandle = "meepcalc"
	if 'acct' in modarg[0]:
		acct = modarg[1]
	if 'procs' in modarg[0]:
		procs = modarg[1]
	if 'aval' in modarg[0]:
		aval = float(modarg[1])
	if procs is None:
		print "Defaulting to 1 processor"
		procs = "1"
	if acct is None:
		print "Defaulting to b1010 account"
		acct = 'b1010'

#STRUCTURES
#imports the geometric objects in the comp cell including location, size and dielectric material
instream = open(inputfile,"r")
importline = False
TempStrutures = []
struct_count = 0
#finds total number of structures in the file
for line in instream:
	if '#ENDSTRUCTURES' in line:
		importline = False
	if importline is True:
		if '#OBJ' in line:
			struct_count += 1
		TempStrutures.append(line)
	if '#STRUCTURES' in line:
		importline = True
instream.close()

#makes an array to contain the structures
Structures = []
for ii in range(struct_count):
	Structures.append([])

importline = False
object_num = 0
for arg in TempStrutures:
	modarg = arg.split()
	if '#ENDOBJ' in modarg[0]:
		importline = False
		object_num += 1
	if importline is True:
		Structures[object_num].append(arg)
	if '#OBJ' in modarg[0]:
		importline = True

STR2 = []
for object in Structures:
	temp = {}
	for param in range(len(object)):
		temp["%s" % object[param].split()[0]] = object[param].split()[1]
	STR2.append(temp)
Structures = STR2
STR2 = []

print "There are %s structure(s):" % len(Structures)
for object in Structures:
	print object

#BOUNDARY
#Gets info on pml, periodicity, other boundary conditions
instream = open(inputfile,"r")
importline = False
BoundArgs = []
for line in instream:
	if '#ENDBOUNDARY' in line:
		importline = False
	if importline is True:
		BoundArgs.append(line)
	if '#BOUNDARY' in line:
		importline = True
instream.close()

BND = {}
for bound in BoundArgs:
	BND["%s" % bound.split()[0]] = bound.split()[1]
BoundInfo = BND
print BoundInfo

#SOURCE
#All information to specify the light source
instream = open(inputfile,"r")
importline = False
TempSources = []
source_count = 0
#finds total number of structures in the file
for line in instream:
	if '#ENDSOURCE' in line:
		importline = False
	if importline is True:
		if '#SRC' in line:
			source_count += 1
		TempSources.append(line)
	if '#SOURCE' in line:
		importline = True
instream.close()

#makes an array to contain the structures
Sources = []
for ii in range(source_count):
	Sources.append([])

importline = False
source_num = 0
for arg in TempSources:
	modarg = arg.split()
	if '#ENDSRC' in modarg[0]:
		importline = False
		source_num += 1
	if importline is True:
		Sources[source_num].append(arg)
	if '#SRC' in modarg[0]:
		importline = True

SRC2 = []
for source in Sources:
	temp = {}
	for param in range(len(source)):
		temp["%s" % source[param].split()[0]] = source[param].split()[1]
	SRC2.append(temp)
Sources = SRC2
SRC2 = []

print "There are %s source(s):" % len(Sources)
for source in Sources:
	print source

#RUNINFO
#Information about the runtime of the calculation
instream = open(inputfile,"r")
importline = False
RunArgs = []
for line in instream:
	if '#ENDRUNINFO' in line:
		importline = False
	if importline is True:
		RunArgs.append(line)
	if '#RUNINFO' in line:
		importline = True
instream.close()

for arg in RunArgs:
	modarg = arg.split()
	if 'flux' in modarg[0]:
		CalcFlux = modarg[1]
	if 'runtime' in modarg[0]:
		RunTime = float(modarg[1])

#OUTPUTS

instream = open(inputfile,"r")
importline = False
OutArgs = []
for line in instream:
	if '#ENDOUTPUTS' in line:
		importline = False
	if importline is True:
		OutArgs.append(line)
	if '#OUTPUTS' in line:
		importline = True
instream.close()

for arg in OutArgs:
	arg = arg.split()
	if len(arg) < 5:
		print "Error: There's an output parameter missing."
		exit(-1)

#**********************************************************************
# Converts LD model to meep dielectric units, based on Rakic1998
#	a: meep normalization const
#	wp: plasma freq in eV
#	fGw0_list: nested list of
#	f oscillator strengths
#	Gamma relaxation in eV
# omega0 in eV,w=0 is handled by converting it to a very small no.
#**********************************************************************

#Metal plasma frequencies in eV
AgPlasFreq = 9.01
AuPlasFreq = 9.03
CuPlasFreq = 10.83
AlPlasFreq = 14.98

#LD Params, nested list of oscillator strengths, Gamma, omega values
AgLDParams = [[0.845,0.048,0.0],[0.065,3.886,0.816],[0.124,0.452,4.481],[0.011,0.065,8.185],[0.840,0.916,9.083],[5.646,2.419,20.29]]
AuLDParams = [[0.760,0.053,0.0],[0.024,0.241,0.415],[0.010,0.345,0.830],[0.071,0.870,2.969],[0.601,2.494,4.304],[4.384,2.214,13.32]]
CuLDParams = [[0.575,0.030,0.0],[0.061,0.378,0.291],[0.104,1.056,2.957],[0.723,2.213,5.300],[0.638,4.305,11.18]]
AlLDParams = [[0.523,0.047,0.0],[0.227,0.333,0.162],[0.050,0.312,1.544],[0.166,1.351,1.808],[0.030,3.382,3.473]]

def meepfactor(a):return 2.0*np.pi*c/a #2pi*c/a
def eV2w(eV):return eV*(2*np.pi)/4.135666e-15
def eV2meep(a,eV):return eV2w(eV)/meepfactor(a)
def sigmaa(f,wp,w):return (f*wp**2)/w**2
def eVLD2meepL(a,wp,fGw0_list):
	oGs_list=[]
	smallno=1e-20;
	for f,G,w0 in fGw0_list:
		if w0==0:
			w0=smallno #hack
		oGs_list.append([eV2meep(a,w0),eV2meep(a,G),sigmaa(f,eV2meep(a,wp),eV2meep(a,w0))])
 	return oGs_list

a_SI = aval * 1.0e-9 #Convert aval to SI units

#Construct list of Meep compatible dielectric parameters
Ag = eVLD2meepL(a_SI,AgPlasFreq,AgLDParams)
Au = eVLD2meepL(a_SI,AuPlasFreq,AuLDParams)
Cu = eVLD2meepL(a_SI,CuPlasFreq,CuLDParams)
Al = eVLD2meepL(a_SI,AlPlasFreq,AlLDParams)
MaterialDatabase = {
	'Ag'	: 	Ag,
	'Au'	:	Au,
	'Cu'	: 	Cu,
	'Al'	: 	Al
}

#**********************************************************************
# Creates a meep control file to be submitted to meep
# File is written in Scheme
# First creates a new directory in which to place the calculations
# Computational volume printes to file here
#**********************************************************************

num = 1
fh_orig = fhandle
while(1):
	if not os.path.exists(fhandle):
		break
	else:
		fhandle = fh_orig + "%i" % num
		num += 1

os.makedirs(fhandle)
shutil.copyfile(inputfile,fhandle + '/' + inputfile)
os.chdir(fhandle)
os.system("mv %s %s" % (inputfile, fhandle + ".txt"))

CWD = os.getcwd()
ctlname = CWD + '/' + fhandle + '.ctl'
c = open(ctlname,"w")

########################################################
# Specify the size of the computational cell, resolution
########################################################
cw = c.write
cw("""\
(set! geometry-lattice
	(make lattice
		(size %s %s %s)
	)
)
""" % (str(CellSize.x),str(CellSize.y),str(CellSize.z))\
)
try:
	cw("(set! resolution %s)" % resolution)
except:
	print "Error: Resolution not provided."
	exit()

# Define all structure parameters
cw("""\
\n(set! geometry
	(list""")

def print_polarizations(material,write_function):
	wf = write_function
	wf("\n					(polarizations")
	for pole in material:
		wf("""\n\
						(make polarizability
							(omega %s)
							(gamma %s)
							(sigma %s)
						) """ % (pole[0], pole[1], pole[2]))
	wf("\n					)")
	return

###############################
# Specify the geometric objects
###############################

for OBJ in Structures:
	num = OBJ.get('type',0)
	if num == 0:
		print "Error: Missing \'type\' in an object description."
		exit()
	if OBJ['type'] not in ['block', 'cone', 'cylinder','sphere','ellipsoid','elps','sphr','cyld']:
		print "Error: Structure type is undefined."
		exit(-1)

#######
#Blocks
#######
	if OBJ['type'] == 'block':
		cw("\n		(make block")
		try:
			center = makexyz(OBJ['center'],"")
			cw("\n			(center %s %s %s)" % (str(center.x),str(center.y),str(center.z)))
		except:
			print "Object missing center coordinates"
			exit()

		try:
			size = makexyz(OBJ['size'],"")
			cw("\n			(size %s %s %s)" % (str(size.x),str(size.y),str(size.z)))
		except:
			print "Object missing size"
			exit()

		try:
			e1 = makexyz(OBJ['e1'],"")
			cw("			(e1 %s %s %s)" % (str(e1.x),str(e1.y),str(e1.z)))
		except:
			e1 = None

		try:
			e2 = makexyz(OBJ['e2'],"")
			cw("			(e2 %s %s %s)" % (str(e2.x),str(e2.y),str(e2.z)))
		except:
			e2 = None

		try:
			e3 = make(OBJ['e3'],"")
			cw("			(e3 %s %s %s)" % (str(e3.x),str(e3.y),str(e3.z)))
		except:
			e3 = None

		try:
			material = OBJ['material']
		except:
			print "Material specification missing"
			exit()

		try:
			material = float(material)
			cw("""\n\
			(material
                (make dielectric
                    (epsilon %s)
                )
            )
""" % str(material))
		except:
			cw("""\n\
			(material
                (make dielectric
                    (epsilon 1.000001)""")
			print_polarizations(MaterialDatabase[material],cw)
			cw("""\n\
                )
            )""")

		cw("""\n		)""")
########
#Spheres
########
	if OBJ['type'] == 'sphere' or OBJ['type'] == 'sphr':
		cw("\n		(make sphere")
		try:
			center = makexyz(OBJ['center'],"")
			cw("\n			(center %s %s %s)" % (str(center.x),str(center.y),str(center.z)))
		except:
			print "Object missing center coordinates"
			exit()

		try:
			radius = OBJ['radius']
			cw("\n			(radius %s)" % radius)
		except:
			print "Object missing radius"
			exit()

		try:
			material = OBJ['material']
		except:
			print "Material specification missing"
			exit()

		try:
			dielec = float(material)
			cw("""\n\
			(material
				(make dielectric
					(epsilon %s)
				)
			)\n""" % material)
		except:
			cw("""\n\
			(material
				(make dielectric
					(epsilon 1.0)""")
			print_polarizations(MaterialDatabase[material],cw)
			cw("""\n\
				)
			)""")

		cw("""\n		)""")

##########
#Cylinders
##########
	if OBJ['type'] == 'cylinder' or OBJ['type'] == 'cyld':
		cw("\n		(make cylinder")
		try:
			center = makexyz(OBJ['center'],"")
			cw("\n			(center %s %s %s)" % (str(center.x),str(center.y),str(center.z)))
		except:
			print "Object missing center coordinates"
			exit()

		try:
			axis = makexyz(OBJ['axis'],"")
			cw("\n			(axis %s %s %s)" % (str(axis.x),str(axis.y),str(axis.z)))
		except:
			axis = None

		try:
			radius = OBJ['radius']
			cw("\n			(radius %s)" % str(radius))
		except:
			print "Missing cylinder radius"
			exit()

		try:
			height = OBJ['height']
			cw("\n			(height %s)" % str(height))
		except:
			print "Missing cylinder height"
			exit()

		try:
			material = OBJ['material']
		except:
			print "Material specification missing"
			exit()

		try:
			material = float(material)
			cw("""\n\
			(material
                (make dielectric
                    (epsilon %s)
                )
            )
""" % str(material))
		except:
			cw("""\n\
			(material
                (make dielectric
                    (epsilon 1.0)""")
			print_polarizations(MaterialDatabase[material],cw)
			cw("""\n\
                )
            )""")

		cw("""\n		)""")

###########
#Ellipsoids
###########
	if OBJ['type'] == 'ellipsoid' or OBJ['type'] == 'elps':
		cw("\n		(make ellipsoid")
		try:
			center = makexyz(OBJ['center'],"")
			cw("\n			(center %s %s %s)" % (str(center.x),str(center.y),str(center.z)))
		except:
			print "Object missing center coordinates"
			exit()

		try:
			size = makexyz(OBJ['size'],"")
			cw("\n			(size %s %s %s)" % (str(size.x),str(size.y),str(size.z)))
		except:
			print "Object missing size"
			exit()

		try:
			e1 = OBJ['e1']
			cw("			(e1 %s %s %s)" % (str(e1.x),str(e1.y),str(e1.z)))
		except:
			e1 = None

		try:
			e2 = OBJ['e2']
			cw("			(e2 %s %s %s)" % (str(e2.x),str(e2.y),str(e2.z)))
		except:
			e2 = None

		try:
			e3 = OBJ['e3']
			cw("			(e3 %s %s %s)" % (str(e3.x),str(e3.y),str(e3.z)))
		except:
			e3 = None

		try:
			material = OBJ['material']
		except:
			print "Material specification missing"
			exit()

		try:
			material = float(material)
			cw("""\n\
			(material
                (make dielectric
                    (epsilon %s)
                )
            )
""" % str(material))
		except:
			cw("""\n\
			(material
                (make dielectric
                    (epsilon 1.0)""")
			print_polarizations(MaterialDatabase[material],cw)
			cw("""\n\
                )
            )""")

		cw("""\n		)""")

######
#Cones
######
	if OBJ['type'] == 'cone':
		cw("\n		(make cone")
		try:
			center = makexyz(OBJ['center'],"")
			cw("\n			(center %s %s %s)" % (str(center.x),str(center.y),str(center.z)))
		except:
			print "Object missing center coordinates"
			exit()

		try:
			axis = makexyz(OBJ['axis'],"")
			cw("\n			(axis %s %s %s)" % (str(axis.x),str(axis.y),str(axis.z)))
		except:
			axis = None

		try:
			radius = OBJ['radius']
			cw("\n			(radius %s)" % str(radius))
		except:
			print "Missing cone radius"
			exit()

		try:
			radius2 = OBJ['radius2']
			cw("\n			(radius2 %s)" % str(radius2))
		except:
			print "Missing cone radius2"
			exit()

		try:
			height = OBJ['height']
			cw("\n			(height %s)" % str(height))
		except:
			print "Missing cone height"
			exit()

		try:
			material = OBJ['material']
		except:
			print "Material specification missing"
			exit()

		try:
			material = float(material)
			cw("""\n\
			(material
                (make dielectric
                    (epsilon %s)
                )
            )
""" % str(material))
		except:
			cw("""\n\
			(material
                (make dielectric
                    (epsilon 1.0)""")
			print_polarizations(MaterialDatabase[material],cw)
			cw("""\n\
                )
            )""")

		cw("""\n		)""")

cw("""\n\
	)
)""")

####################
# Define the Sources
####################

#############################
# Check for oblique incidence
#############################

oblique_vect = 0.0
for SRC in Sources:
		num = SRC.get('angle',0)
		if num != 0:
			print "Setting up oblique incidence..."
			oblique_vect = np.sin((np.pi/180.0)*float(SRC['angle']))
			try:
				FREQ = 1.0/float(SRC['wavelength'])
			except:
				FREQ = 0.0
			oblique_vect *= FREQ
			cw("\n(define (my-amp-func p) (exp (* 2 %f %f (vector3-x p))))" % (np.pi,oblique_vect))
			cw("\n(set! k-point (vector3 %f 0 0))" % oblique_vect)
			break

cw("""\n\
(set! sources
	(list
""")
for SRC in Sources:
	num = SRC.get('type',0)
	if num == 0:
		print "Error: Missing \'type\' in a source description."
		exit()
	if SRC['type'] not in ['gaussian','cont','continuous']:
		print "Error: source type undefined"
		exit(-1)

############
# CONTINUOUS
############

	if SRC['type'] == 'continuous' or SRC['type'] == 'cont':
		cw("""\n\
		(make source
			(src
				(make continuous-src""")
		try:
			wavelength = SRC['wavelength']
			cw("\n					(wavelength %s)" % str(wavelength))
		except:
			print "Error: no information about the source wavelength has been provided."
			exit()

		try:
			start = SRC['start']
			cw("\n					(start-time %s)" % str(start))
		except:
			print "No source start time provided. Defaulting to 0."

		try:
			end = SRC['end']
			cw("\n					(end-time %s)" % str(end))
		except:
			print "No source end time provided. Source will not turn off."

		try:
			width = SRC['width']
			cw("\n					(width %s)" % str(width))
		except:
			print "No width provided."

		try:
			cutoff = SRC['cutoff']
			cw("\n					(cutoff %s)" % str(cutoff))
		except:
			print "No cutoff provided."

		cw("""\n				)
			)""")

		try:
			component = SRC['polarization']
		except:
			print "Error: no light polarization provided."
			exit()

		if component not in ['Ex','Ey','Ez','Hy','Hx','Hz']:
			print "Error: provided source component is incorrect."
			exit()

		cw("\n			(component %s)" % str(component))

		try:
			center = makexyz(SRC['center'],"")
			cw("\n			(center %s %s %s)" %(center.x,center.y,center.z))
		except:
			print "Error: source center not provided."
			exit()

		try:
			size = makexyz(SRC['size'],"")
			cw("\n			(size %s %s %s)" %(size.x,size.y,size.z))
		except:
			print "Error: source size not provided."
			exit()

		try:
			amp = makexyz(SRC['amplitude'],"")
			cw("\n			(amp %s %s %s)" %(amp.x,amp.y,amp.z))
		except:
			print "No amplitude provided."

		if SRC.get('angle',0) != 0:
			cw("\n 			(amp-func my-amp-func)")

		cw("\n		)")

##########
# GAUSSIAN
##########

	if SRC['type'] == 'gaussian' or SRC['type'] == 'gauss':
		cw("""\n\
		(make source
			(src
				(make gaussian-src""")
		try:
			wavelength = SRC['wavelength']
			cw("\n					(wavelength %s)" % str(wavelength))
		except:
			print "Error: no information about the source wavelength has been provided."
			exit()

		try:
			start = SRC['start']
			cw("\n					(start-time %s)" % str(start))
		except:
			print "No source start time provided. Defaulting to 0."

		try:
			width = SRC['width']
			cw("\n					(width %s)" % str(width))
		except:
			print "No width provided."

		try:
			cutoff = SRC['cutoff']
			cw("\n					(cutoff %s)" % str(cutoff))
		except:
			print "No cutoff provided."

		cw("""\n				)
			)""")

		try:
			component = SRC['polarization']
		except:
			print "Error: no light polarization provided."
			exit()

		if component not in ['Ex','Ey','Ez','Hy','Hx','Hz']:
			print "Error: provided source component is incorrect."
			exit()

		cw("\n			(component %s)" % str(component))

		try:
			center = makexyz(SRC['center'],"")
			cw("\n			(center %s %s %s)" %(center.x,center.y,center.z))
		except:
			print "Error: source center not provided."
			exit()

		try:
			size = makexyz(SRC['size'],"")
			cw("\n			(size %s %s %s)" %(size.x,size.y,size.z))
		except:
			print "Error: source size not provided."
			exit()

		try:
			amp = makexyz(SRC['amplitude'],"")
			cw("\n			(amp %s %s %s)" %(amp.x,amp.y,amp.z))
		except:
			print "No amplitude provided."

		cw("\n		)")


cw("""\n\
	)
)
""")

###########################
# Define PML's and k-points
###########################

#######
# PML's
#######

PML = BoundInfo.get('pml',0)
if PML == 0:
	print "Error: No PML info provided."
	exit(-1)

if PML not in ['x','+x','-x','y','+y','-y','z','+z','-z','all','none']:
	print "Error: Improper PML info provided."
	exit(-1)

PML_thickness = BoundInfo.get('thickness',-1)
if PML_thickness == -1 and PML is not 'none':
	print "Error: Please provide a PML thickness."
	exit(-1)

if PML == 'all':
	cw("""\n\
(set! pml-layers
    (list
        (make pml
            (thickness %s)
        )
    )
)
""" % PML_thickness)

if PML in ['x','y','z']:
	cw("""\n\
(set! pml-layers
    (list
        (make pml
        	(direction %s)
            (thickness %s)
        )
    )
)
""" % (PML.upper(),PML_thickness))

if PML in ['+x','-x','+y','-y','+z','-z']:
	Side = PML[0]
	if Side == '+':
		PML_Side = "High"
	elif Side == '-':
		PML_Side = "Low"
	Dir = PML[1].upper()
	cw("""\n\
(set! pml-layers
    (list
        (make pml
        	(direction %s)
        	(side %s)
            (thickness %s)
        )
    )
)
""" % (Dir,PML_Side,PML_thickness))

##########
# k-points
##########

KPT = BoundInfo.get('periodic',0)
if KPT == 0:
	print "No k-point information provided."
else:
	kpoint = makexyz(KPT,"")
	if kpoint.x == 1:
		kpoint.x = 0.0 #1.0/float(CellSize.x)
	if kpoint.y == 1:
		kpoint.y = 0.0 #1.0/float(CellSize.y)
	if kpoint.z == 1:
		kpoint.z = 0.0 #1.0/float(CellSize.z)
	if oblique_vect == 0.0: #Using this kpoint and the oblique source kpoint creates problems, so don't print this unless there's no oblique incidence
		cw("""\n\
(set! k-point
    (vector3 %s %s %s)
)""" % (str(kpoint.x),str(kpoint.y),str(kpoint.z)))

################################################
# Define flux regions for frequency calculations
################################################

if CalcFlux == 'true':
	instream = open(inputfile,"r")
	importline = False
	FluxArgs = []
	for line in instream:
		if '#ENDFLUX' in line:
			importline = False
		if importline is True:
			FluxArgs.append(line)
		if '#FLUX' in line:
			importline = True
	instream.close()

	FLX = {}
	for arg in FluxArgs:
		FLX["%s" % arg.split()[0]] = arg.split()[1]
	FluxInfo = FLX

	req_args = ['trans','refl','rsize','tsize','wmin','wmax','NFreq']
	for arg in req_args:
		TEST = FLX.get(arg,0)
		if TEST == 0:
			print "Error: Missing required argument for flux calculation."
			print "Missing %s" % arg
			exit(-1)
	transloc = makexyz(FLX['trans'],"")
	reflloc = makexyz(FLX['refl'],"")
	transsize = makexyz(FLX['tsize'],"")
	reflsize = makexyz(FLX['rsize'],"")
	fcen = 0.5*(1.0/float(FLX['wmin']) + 1.0/float(FLX['wmax']))
	df = 0.5*(1.0/float(FLX['wmin']) - 1.0/float(FLX['wmax']))
	nfreq = FLX['NFreq']

	cw("""\n\
(define trans
	(add-flux %s %s %s
		(make flux-region
			(center %s %s %s)
			(size %s %s %s)
		)
	)
) """ % (str(fcen), str(df), nfreq, str(transloc.x), str(transloc.y), str(transloc.z), str(transsize.x), str(transsize.y), str(transsize.z) ) )
	cw("""\n\
(define refl
	(add-flux %s %s %s
		(make flux-region
			(center %s %s %s)
			(size %s %s %s)
		)
	)
) """ % (str(fcen), str(df), nfreq, str(reflloc.x), str(reflloc.y), str(reflloc.z), str(reflsize.x), str(reflsize.y), str(reflsize.z) ) )


############################
# Run and Output information
############################

#Uses the center of the transmission region as the point at which to monitor the field decay
if CalcFlux == 'true':
	cw("""\n\
(run-sources+
	(stop-when-fields-decayed %s %s (vector3 %s %s %s) 1e-4)
""" % (RunTime,\
	Sources[0]['polarization'],\
	str(transloc.x), \
	str(transloc.y), \
	str(transloc.z)))

else:
	cw("""\n\
(run-until %s
""" % str(RunTime))

cw("""\n\
	(to-appended \"eps\" (at-beginning output-epsilon))
	(to-appended \"final_dpwr\" (at-end output-dpwr))
""")

print "Determining outputs..."
for ARG in OutArgs:
	arg = ARG.split()
	component = arg[0]
	center = makexyz(arg[1],"")
	size = makexyz(arg[2],"")
	time_int = arg[3]
	suffix = arg[4]
	if component == 'dpwr':
		cw("\n\t(to-appended \"dpwr\" (at-every %s output-dpwr))" % time_int)
	else:
		cw("""\n\
	(to-appended \"%s\"
		(at-every %s
			(in-volume
				(volume
					(center %s %s %s)
					(size %s %s %s)
				)
			output-%sfield-%s
			)
		)
	)
""" % (suffix, time_int, str(center.x),str(center.y),str(center.z),str(size.x),str(size.y),str(size.z),component.lower()[0],component[1]) )

#Print output statements here

cw("\n)")

if CalcFlux == 'true':
	cw("\n(display-fluxes trans refl)")

c.close()


###############################################
# Make job submission script and submit to MOAB
###############################################

subfile = open("RunFDTD.sh","w")
subfile.write("""
#!/bin/bash
#MOAB -l walltime=4:00:00
#MOAB -l nodes=1:ppn=%s
#MOAB -j oe
#MOAB -A b1010
#MOAB -N %s

module load meep
cd %s

meep-mpi %s

	""" % (procs,fhandle,CWD,ctlname))

subfile.close()
os.system("msub RunFDTD.sh")


#	Run calibration files

#	Calculate |E|^2/|E0|^2, print to file

#	Create plot of the trapping potential

#	Find the plot minima and maxima
#		Print labels on plots?

#	Density matrix considerations?
#	This might be needed to get the trapping potential
