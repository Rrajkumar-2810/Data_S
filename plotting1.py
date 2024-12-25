from matplotlib import pyplot as plt
x = [42, 61, 78, 23, 42]
y = [45, 84, 56, 75, 45]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x, y, linewidth=5, linestyle='solid', color='green')
plt.show()
