class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def display_info(self):
        print("Product: " + self.name + "\n Price: " + str(self.price) + "\n Quantity: " + str(self.quantity) + "\n Total Cost: " + str(self.total_cost()))


product1 = Product("Laptop", 55000, 2)
product2 = Product("Smartphone", 30000, 3)
product3 = Product("Headphones", 2000, 5)

product1.display_info()
product2.display_info()
product3.display_info()

