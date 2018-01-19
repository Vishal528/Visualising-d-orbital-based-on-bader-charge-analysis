import numpy
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import randn
from scipy import array, newaxis
#Co-ordinates of the 3-d grid is stored in list A
A = []
for i in range(120):
    for j in range(120):
        for k in range(120):
                A.append([k/119*10.460582,j/119*10.460582,i/119*10.46052])

#The charge density matrix is loaded
B = numpy.loadtxt('CHGCAR')

#Reshaping the charge density matrix so that there is a one-one correspondance between a co-ordinate and its charge density value
B = numpy.reshape(B,120*120*120)
B = B.tolist()

#Sorting the list in asecending oreder of charge densities and store the indices it in sort_idx
sort_idx = numpy.argsort(B)
#Storing the corresponding co-ordinates to that of the charge charge density values
L=[]
[L.append(A[idx]) for idx in sort_idx]

#Taking top 100000 values and converting the list into an array so that it can be used in plotting the surface
M = array(L[len(L)-100000:len(L)])

#3-D surface plot of the points
Xs = M[:,0]
Ys = M[:,1]
Zs = M[:,2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)

ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.zaxis.set_major_locator(MaxNLocator(5))

fig.tight_layout()

plt.show()
