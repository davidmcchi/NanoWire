mport numpy as np
import sys

if len(sys.argv) < 3:
    print "Please provide an input and an output file."
    exit()
filename = open(sys.argv[1],"r")
out = open(sys.argv[2],"w")
y = 0
for line in filename:
	nums = line.split(',')
	x = 0
	for n in nums:
		out.write("%i %i %s\n" % (y,x,n))
		x += 1
	y += 1
	out.write("")
