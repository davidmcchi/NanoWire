import numpy as np
import matplotlib.pyplot as plt


filename = "C:\Users\David Chi\Desktop\Summer Quarter\Summer Research\Enthought\AgFilmX-3col.txt"

x = np.genfromtxt(filename,usecols=(0))
nx = int(max(x)+1)

y = np.genfromtxt(filename,usecols=(1))
ny = int(max(y)+1)

z = np.genfromtxt(filename,usecols=(2))

data = np.zeros((nx,ny),dtype=float)
 
for X,Y,Z in zip(x,y,z):
    data[int(X)][int(Y)] = Z


#refer to Boring slide show code

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
cmin = min(z)
cmax = max(z)
numxtics = 3 
numytics = 5
numctics = 5

"""p = plt.imshow(data)
plt.show()
fig = plt.gcf()
plt.clim()
plt.title("FDTD Plotting")

plt.pcolor(X, Y, data, cmap=cm, vmin=-4, vmax=4)
plt.colorbar()
"""

figure = plt.Figure()
axes = figure.add_subplot(111)


xticks = np.linspace(xmin, xmax, numxtics)
yticks = np.linspace(ymin, ymax, numytics)
cticks = np.linspace(cmin,cmax, numctics)

axes.set_xlim([xmin, xmax])
axes.set_ylim([ymin, ymax])

axes.xaxis.set_ticks(xticks)
axes.yaxis.set_ticks(yticks)

axes.tick_params(axis='x',which='both',bottom='on',top='off',direction='out',width=1.5)
axes.tick_params(axis='y',which='both',left='on',right='off',direction='out',width=1.5)

axes.set_xticklabels(xticks,fontweight='bold',fontsize=12)
axes.set_yticklabels(yticks,fontweight='bold',fontsize=12)

axes.set_xlabel("X-plane / nm" , fontweight='bold',fontsize=12)
axes.set_ylabel("Y-plane / nm" , fontweight='bold',fontsize=12)

t = axes.set_title(r'$\mathbf{|\vec{E}|^2/ |\vec E_0|^2}$', fontweight='bold',fontsize=12)
t.set_y(1.04) 							#Offset the title so it doesn't overlap with the plot
im = axes.imshow(data, cmap="jet",origin='lower',extent=[xmin,xmax,ymin,ymax])
im.set_clim(cmin,cmax) 		#Set the colorbar limits
cbar = figure.colorbar(im, ticks = cticks)
cbar.ax.set_yticklabels(cticks,fontweight='bold',fontsize=12)


plt.show()

"""plt.subplot(1, 3, n)
plt.pcolor(X, Y, f(data), cmap=cm, vmin=-4, vmax=4)"""

# from Josh's code
"""
figure = plt.Figure()							#Figure needed to plot cbar
		axes = figure.add_subplot(111)			#For the heatmap
		canvas = FigureCanvas(self, -1, figure)	#No canvas, no plot
		axes.cla()										#Clear if anything was left. I don't know why I need this, but it improves functionality

		#Define all parameters for the tick locations, axis limits, labels etc...
		xticks = np.linspace(xmin, xmax, numxtics)
		yticks = np.linspace(ymin, ymax, numytics)
		cticks = np.linspace(cmin,cmax,numctics)

		axes.set_xlim([xmin, xmax])
		axes.set_ylim([ymin, ymax])

		axes.xaxis.set_ticks(xticks)
		axes.yaxis.set_ticks(yticks)

		axes.tick_params(axis='x',which='both',bottom='on',top='off',direction='out',width=1.5)
		axes.tick_params(axis='y',which='both',left='on',right='off',direction='out',width=1.5)

		axes.set_xticklabels(xticks,fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize'])
		axes.set_yticklabels(yticks,fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize'])

		axes.set_xlabel("X-plane / %i nm" % int(GetGrandParent().fdtd.aval), fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize'])
		axes.set_ylabel("Y-plane / %i nm" % int(GetGrandParent().fdtd.aval), fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize'])

		t = axes.set_title(r'$\mathbf{|\vec{E}|^2/ |\vec E_0|^2}$', fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize']+1)
		t.set_y(1.04) 							#Offset the title so it doesn't overlap with the plot
		im = axes.imshow(GetGrandParent().fdtd.EMF,cmap=color,origin='lower',alpha=0.9,extent=[xmin,xmax,ymin,ymax])
		im.set_clim(cmin,cmax) 		#Set the colorbar limits
		cbar = figure.colorbar(im, ticks = cticks)
		cbar.ax.set_yticklabels(cticks,fontweight='bold',fontsize=GetGrandParent().plotparams['Font']['fontsize'])
"""

#print nx,ny

#plt.imshow(data)
