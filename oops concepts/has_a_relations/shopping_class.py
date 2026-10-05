class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "-", self.price)


class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 1000),
            Product("Keyboard", 2000)
        ]

    def show_products(self):
        for product in self.products:
            product.display()


cart = ShoppingCart()
cart.show_products()