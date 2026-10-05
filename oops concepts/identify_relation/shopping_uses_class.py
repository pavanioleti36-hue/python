class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "completed")
class ShoppingCart:
    def __init__(self, amount):
        self.amount = amount
    def checkout(self, gateway):
        gateway.pay(self.amount)
cart = ShoppingCart(1600)
gateway = PaymentGateway()
cart.checkout(gateway)