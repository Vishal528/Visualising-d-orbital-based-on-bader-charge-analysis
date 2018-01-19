# Visualising d orbital based on charge density calculations

 Overview
 ============
 * The file CHGCAR contains charge density values for Pt atom. 
 * The Pt atom is located at [0.5,0.5,0.5] in space.
 * The points where the charge densities are calculated are basically of a 120*120*120 grid of a square of side length 10.460582 units in the first ocatant of the 3-d space.
 
 Dependencies
 ============
 * numpy
 * sys
 * matplotlib
 * scipy
 * mpl_toolkits 
 * Install any missing dependicies using pip. E.x. pip3 install numpy 

 Functioning
 ============
 * The code in plot.py does the following :
 * Sorts the charge density matrix based on its values in ascending order
 * The coordinates corresponding to the top 100000 charge density values are plotted and a 3-d surface which is similar to that of a lobe of a d orbital is obtained.
 * The number of coordinated to be plotted can be increased and it can be observed that flucations are induced when we consider more number of points because here the surface is plotted just on the basis of sorting not by accessing every direction.

 Usage 
 ============
 * Run plot.py in terminal

