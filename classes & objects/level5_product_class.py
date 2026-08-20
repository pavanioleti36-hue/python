class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print("Product: " + self.name)
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))
        print("Total Price: " + str(self.total_price()))


product1 = Product("Laptop", 55000, 2)
product2 = Product("Smartphone", 30000, 3)
product3 = Product("Headphones", 2000, 5)

product1.display_info()
print()
product2.display_info()
print()
product3.display_info()
