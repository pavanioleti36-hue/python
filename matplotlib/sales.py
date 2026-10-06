import matplotlib.pyplot as plt
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [150, 200, 300, 250]
plt.plot(products, sales, linestyle='--', marker='X')
plt.title("Sales Data")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()