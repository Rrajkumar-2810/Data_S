from matplotlib import pyplot as plt
import numpy as np

# plotting of two bar charts in one
company = ["Google","Amazon","Microsoft","Facebook"]
revenue = [90,136,89,27]
profit = [40,2,34,12]

xpos = np.arange(len(company))
print("X-Positions:",xpos)

plt.xticks(xpos, company)
plt.ylabel("Revenue")
plt.title("Us Tech Stocks")

plt.bar(xpos-0.2, revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2, profit, width=0.4, label="Profit")
plt.legend(loc="best")
#plt.bar(company, revenue, color="red")
plt.show()
