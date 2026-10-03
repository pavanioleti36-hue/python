from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")
class Card(Payment):
    def pay(self):
        print("Payment made using Card")
class NetBanking(Payment):
    def pay(self):
        print("Payment made using Net Banking")
upi = UPI()
card = Card()
netbanking = NetBanking()
upi.pay()
card.pay()
netbanking.pay()