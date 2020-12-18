"""
The Feigenbaum_Plot.py generate the Feigenbaum_Plot using two initial parameters x and r.
(https://en.wikipedia.org/wiki/Bifurcation_diagram)



"""


import matplotlib.pyplot as plt, numpy as np,
from numpy import arange
from math import pi, sqrt, pow

print("The following program generate the Feigenbaum Plot using x'=rx(1-x)")
#r = float(input("Please enter the initial r value > "))
#x = float(input("Please enter the starting point > "))

r=1
xi=0.5

#The two vector to store the values of y and r
y_vec = []
r_vec = []



x=xi
for ir in arange (r,4,0.0015):
    for i in range(1,1000+1):
        y = ir*x*(1.0 - x)
        x=y
        #Print the values to check that all is correct
        #print(f"The {i} point is ({ir},{y})")
        y_vec.append(y)
        r_vec.append(ir)

#Ausiliar print to check that all is correct.
#print(r_vec)
#print(" ")
#print(y_vec)

#Print the results in a file in two columns
name_file ="Feigenbaum_Plot_V1_r_{}_x_{}.txt".format(r,xi)

out_file = open(name_file,'w')
np.savetxt(name_file, np.column_stack((r_vec, y_vec)),fmt="%1.16f %1.16f")
out_file.close()
#---------------------------------------------------------------


#Plot of Feigenbaum points
plt.rc('font', family='serif')
plt.title(f"Feigenbaum_Plot_V1_r_{r}_x_{xi}")
plt.plot(r_vec,y_vec,linestyle="None",marker='o',markersize=1,color="black")
plt.ylabel("y")
plt.xlabel('r')
plt.savefig("Feigenbaum_Plot_V1_r_{}_x_{}.png".format(r,xi))
plt.show()