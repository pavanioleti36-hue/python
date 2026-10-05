class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "completed successfully")


class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self, gateway):
        gateway.pay(self.total)


cart = ShoppingCart(2500)
gateway = PaymentGateway()

cart.checkout(gateway)