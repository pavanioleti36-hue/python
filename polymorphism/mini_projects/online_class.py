class UPI:
    def pay(self, amount):
        print("Paid ", amount, "using UPI")
class CreditCard:
    def pay(self, amount):
        print("Paid ", amount, "using Credit Card")
class NetBanking:
    def pay(self, amount):
        print("Paid ", amount, "using Net Banking")
payment_methods = [UPI(), CreditCard(), NetBanking()]
for payment in payment_methods:
    payment.pay(2500)