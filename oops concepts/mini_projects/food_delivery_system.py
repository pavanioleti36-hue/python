class Order:
    def __init__(self,amount):
        self.amount=amount
class OnlineOrder(Order):
    def online(self):
        print("Online order placed")
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Restaurant:
    def __init__(self):
        self.menu=[MenuItem("Pizza",300),MenuItem("Burger",150)]
class PaymentService:
    def pay(self,amount):
        print("Payment:",amount)
class DeliveryService:
    def deliver(self):
        print("Food delivered")
order=OnlineOrder(450)
restaurant=Restaurant()
order.online()
PaymentService().pay(order.amount)
DeliveryService().deliver()