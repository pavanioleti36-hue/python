class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "completed")
class ShoppingCart:
    def __init__(self):
        self.products = [Product("Laptop", 50000), Product("Mouse", 1000)]
    def checkout(self, gateway):
        total = 0
        for product in self.products:
            total += product.price
        gateway.pay(total)
cart = ShoppingCart()
gateway = PaymentGateway()
cart.checkout(gateway)