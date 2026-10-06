from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

    def refund(self):
        print("UPI Refund")

class CreditCard(Payment):
    def pay(self):
        print("Credit Card Payment")

    def refund(self):
        print("Credit Card Refund")

class NetBanking(Payment):
    def pay(self):
        print("Net Banking Payment")

    def refund(self):
        print("Net Banking Refund")

u = UPI()
c = CreditCard()
n = NetBanking()
u.pay()
u.refund()
c.pay()
c.refund()
n.pay()
n.refund()