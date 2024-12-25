from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]
z = [45,84,56,75,45,74,61]
a = [51,74,91,34,49,28,39]
plt.plot(x,y, 'g*-.', markersize=8) #color=, marker=, linestyle=
plt.plot(x,z, 'r+-.', markersize=16) #color=, marker=, linestyle=
plt.plot(x,a, 'r+-.', markersize=20, alpha=0.5) #alpha - determines the opaqueness of the graph 
plt.show()
