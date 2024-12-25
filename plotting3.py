from matplotlib import pyplot as plt
days = [1,2,3,4,5,6,7]
max_t = [50,51,52,48,47,49,46]
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,40,42,41]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(days,max_t, 'g*-.', markersize=8, label="Max") #color=, marker=, linestyle=
plt.plot(days,min_t, 'r+-.', markersize=14, label="Min") #color=, marker=, linestyle=
plt.plot(days,avg_t, 'bd-.', markersize=18, alpha=0.5, label="Avg") #color=, marker=, linestyle=
plt.legend(loc="best", shadow=True, fontsize="small")
plt.grid()
plt.show()
