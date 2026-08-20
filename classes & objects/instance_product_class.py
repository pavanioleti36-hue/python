class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product1 = Product("Laptop", 50000, 2)
product2 = Product("Phone", 20000, 3)
product3 = Product("Headphones", 1500, 5)
print("Total Price of", product1.name, ":", product1.total_price())
print("Total Price of", product2.name, ":", product2.total_price())
print("Total Price of", product3.name, ":", product3.total_price())