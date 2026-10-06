import matplotlib.pyplot as plt
months= ["jan","feb","mar","apr"]
sales= [10, 30, 40, 20]
plt.plot(months, sales) 
plt.savefig("sales_chart.png")
plt.show()