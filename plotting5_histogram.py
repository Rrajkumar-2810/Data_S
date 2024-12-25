from matplotlib import pyplot as plt
import numpy as np
#Using only one dataset for histogram

blood_sugar = [133, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
#plt.hist(blood_sugar, bins=3, rwidth=0.95)
#plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, color='r', histtype='step') #Looks like steps
plt.hist(blood_sugar, bins=3, rwidth=0.95, color='r')

plt.show()
