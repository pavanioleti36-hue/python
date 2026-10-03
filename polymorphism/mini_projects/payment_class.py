class UPI:
    def pay(self, amount):
        print("Paid ", amount, "using UPI")
class CreditCard:
    def pay(self, amount):
        print("Paid ", amount, "using Credit Card")
class DebitCard:
    def pay(self, amount):
        print("Paid ", amount, "using Debit Card")
class NetBanking:
    def pay(self, amount):
        print("Paid ", amount, "using Net Banking")
payments = [UPI(), CreditCard(), DebitCard(), NetBanking()]
for payment in payments:
    payment.pay(1000)