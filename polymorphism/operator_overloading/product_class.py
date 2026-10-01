class Product:
    def __init__(self, price):
        self.price = price
    def __add__(self, other):
        return self.price + other.price
p1 = Product(1000)
p2 = Product(1500)
print("Combined Price:", p1 + p2)