from matplotlib import pyplot as plt
import numpy as np

exp_vals = [1400, 600, 300, 410, 250]
exp_labels = ["Home rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]
plt.axis("equal")
plt.pie(exp_vals, labels=exp_labels, radius=0.8, autopct='%0.2f%%',
        shadow=True, explode=[0,0.2,0,0,0], startangle=180)

#radius = change the size of the circle
#autopct = to display numbers in the pie chart upto decimal point you require 
#shadow = To display a shdow around the parts of the chart
#explode = to display the pie chart parts with separation 
#startangle = gives you the ease to start the piechart in the desired direction by setting an angle
plt.show()
