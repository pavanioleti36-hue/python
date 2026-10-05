class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Laptop(Product):
    def show_type(self):
        print("This is a laptop")
class PaymentService:
    def pay(self,amount):
        print("Payment:",amount)
class DeliveryService:
    def deliver(self):
        print("Product delivered")
class ShoppingCart:
    def __init__(self):
        self.products=[Laptop("Dell",50000),Product("Mouse",1000)]
    def checkout(self,payment,delivery):
        total=sum(p.price for p in self.products)
        payment.pay(total)
        delivery.deliver()
cart=ShoppingCart()
cart.products[0].show_type()
cart.checkout(PaymentService(),DeliveryService())