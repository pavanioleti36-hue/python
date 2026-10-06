import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10000, 15000, 12000, 18000, 20000]
plt.fill_between(months, sales, alpha=0.5)
plt.plot(months, sales, marker='o')
plt.title("Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()