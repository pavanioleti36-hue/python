import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10000, 15000, 12000, 18000, 20000]
plt.plot(months, sales, marker='o')
plt.annotate('Highest Sales', xy=('May', 20000), xytext=('Apr', 22000),
             arrowprops={"arrowstyle": "->"})
plt.show()