import matplotlib.pyplot as plt
products=["laptop","mobile","tablet","desktop","keyboard"]
sales=[150, 200, 300, 250, 100]
plt.barh(products, sales, color='green', )
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()