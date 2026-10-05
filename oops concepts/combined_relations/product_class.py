class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "completed")
class DeliveryService:
    def deliver(self, address):
        print("Order delivered to:", address)
class OnlineOrder:
    def __init__(self):
        self.products = [Product("Phone", 20000), Product("Headphones", 2000)]
    def place_order(self, payment_service, delivery_service):
        total = 0
        for product in self.products:
            total += product.price
        payment_service.pay(total)
        delivery_service.deliver("Hyderabad")
order = OnlineOrder()
payment = PaymentService()
delivery = DeliveryService()
order.place_order(payment, delivery)