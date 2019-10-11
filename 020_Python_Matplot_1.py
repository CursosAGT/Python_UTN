from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Matplot                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                 Cerrar la pantalla para continuar                           ║
╚═════════════════════════════════════════════════════════════════════════════╝
flag R cmd/  flag x simbolo de sistem -> pythom // pythom3 -m pip install
			python -m pip install matplotlib
https://pythonbasics.org/matplotlib-line-chart/
fuente     https://matplotlib.org/
""")
nuevo(0,"inicio");

#################################################################
#Matplot_01
import tkinter
#from io import StringIO
#import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#import imutils

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
	   title='About as simple as it gets, folks')
ax.grid()
plt.title('Hey UTN- que onda????')
print("\tCerrar la pantalla para continuar")
fig.savefig("imagen_desde_Matplot.png")
plt.show()
nuevo(1);
#################################################################
#Matplot_02
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Hey UTN-unamos los puntos con lineas')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.title('Hey UTN-unamos los puntos con ondas')
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(2);
#################################################################
#Matplot_03
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,1]

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Hey UTN -linea')
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(3);
#################################################################
#Matplot_04
import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1, y1, label = "linea 1")

x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x2, y2, label = "linea 2")


plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Hey UTN- dos lineas')
plt.legend()
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(4);
#################################################################
#Matplot_05
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [2,4,1,5,2,6]

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Hey UTN-dashed')
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(5);
#################################################################
#Matplot_06
import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 24, 36, 40, 5]

tick_label = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

plt.bar(left, height, tick_label = tick_label,  width = 0.8, color = ['red', 'green'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Hey UTN-barras')
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(6);
#################################################################
#Matplot_07
import matplotlib.pyplot as plt

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
		60,7,13,57,18,90,77,32,21,20,40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('Hey UTN-histograma-barras')
print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(7);
#################################################################
#Matplot_08
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]

plt.scatter(x, y, label= "stars", color= "green", marker= "*", s=30)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Hey UTN-scatter plot!')

plt.legend()

print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(8);
#################################################################
#Matplot_09
import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
		radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

plt.title('Hey UTN-tortas!')

plt.legend()

print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(9);
#################################################################
#Matplot_010
# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*(np.pi), 0.1)
y = np.sin(x)


plt.plot(x, y)

plt.title('Hey UTN-Seno!')

plt.legend()

print("\tCerrar la pantalla para continuar")
plt.show()
nuevo(10);
#################################################################
#Matplot_011
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
			   origin='lower', extent=[-3, 3, -3, 3],
			   vmax=abs(Z).max(), vmin=-abs(Z).max())

plt.title('Hey UTN-Seno!')
print("\tCerrar la pantalla para continuar")

plt.show()
nuevo(11);
#################################################################
#Matplot_012

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np


# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(1, 5 + dy, dy),
				slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh with levels')


# contours are *point* based plots, so convert our bound into point
# centers
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
				  y[:-1, :-1] + dy/2., z, levels=levels,
				  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf with levels')

# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()

plt.show()
nuevo(12);
#################################################################
#Matplot_013

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	 np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

nuevo(13);
#################################################################
#Matplot_014
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
	(Path.MOVETO, (1.58, -2.57)),
	(Path.CURVE4, (0.35, -1.1)),
	(Path.CURVE4, (-1.75, 2.0)),
	(Path.CURVE4, (0.375, 2.0)),
	(Path.LINETO, (0.85, 1.15)),
	(Path.CURVE4, (2.2, 3.2)),
	(Path.CURVE4, (3, 0.05)),
	(Path.CURVE4, (2.0, -0.5)),
	(Path.CLOSEPOLY, (1.58, -2.57)),
	]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
ax.axis('equal')
plt.show()

nuevo(14);
