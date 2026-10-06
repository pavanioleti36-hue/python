import matplotlib.pyplot as plt
months = ["jan","feb","mar"]
sales = [20,50,10]
customers = [10,25,15]
fig, ax1 = plt.subplots()
ax1.plot(months, sales)
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax2 = ax1.twinx()
ax2.plot(months, customers)
ax2.set_ylabel("Customers")
plt.show()