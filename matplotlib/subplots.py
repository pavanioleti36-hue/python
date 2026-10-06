import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 20, 30, 40, 50]

plt.subplot(2, 2, 1)
plt.plot(months, sales)
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(months, sales)
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.hist(sales)
plt.title("Histogram")

plt.subplot(2, 2, 4)
plt.scatter(range(5), sales)
plt.title("Scatter")

plt.tight_layout()
plt.show()