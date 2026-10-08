from abc import ABC, abstractmethod
class ECommercePayment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(ECommercePayment):
    def pay(self):
        print("Payment using UPI")
class CreditCard(ECommercePayment):
    def pay(self):
        print("Payment using Credit Card")
class DebitCard(ECommercePayment):
    def pay(self):
        print("Payment using Debit Card")
class NetBanking(ECommercePayment):
    def pay(self):
        print("Payment using Net Banking")
payments = [UPI(), CreditCard(), DebitCard(), NetBanking()]
for payment in payments:
    payment.pay()