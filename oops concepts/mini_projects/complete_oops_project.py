class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Electronics(Product):
    def show_type(self):
        print("Electronics:",self.name)
class Clothing(Product):
    def show_type(self):
        print("Clothing:",self.name)
class Customer:
    def __init__(self,name):
        self.name=name
class PaymentService:
    def pay(self,amount):
        print("Payment completed:",amount)
class DeliveryService:
    def deliver(self):
        print("Order delivered")
class ShoppingCart:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
    def total(self):
        return sum(p.price for p in self.products)
class Order:
    def __init__(self,customer,cart):
        self.customer=customer
        self.cart=cart
    def checkout(self,payment,delivery):
        payment.pay(self.cart.total())
        delivery.deliver()
class Store:
    def __init__(self):
        self.products=[Electronics("Laptop",50000),Clothing("Shirt",1000)]
customer=Customer("Pavani")
store=Store()
cart=ShoppingCart()
cart.add_product(store.products[0])
cart.add_product(store.products[1])
order=Order(customer,cart)
store.products[0].show_type()
store.products[1].show_type()
order.checkout(PaymentService(),DeliveryService())