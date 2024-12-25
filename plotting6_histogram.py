from matplotlib import pyplot as plt
import numpy as np

blood_sugar_men = [133, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.xlabel("BLood Sugar Range")
plt.ylabel("No.of People")
plt.title("Patients' Sugar Analysis")
plt.hist([blood_sugar_men,blood_sugar_women], bins=[80,100,125,150], rwidth=0.95,
         color=['r','g'], label=['men','women'])

#plt.hist([blood_sugar_men,blood_sugar_women], bins=[80,100,125,150], rwidth=0.95,
#         color=['r','g'], label=['men','women'], orientation="horizontal")
plt.legend()
plt.show()
