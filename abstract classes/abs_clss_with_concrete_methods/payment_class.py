from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    def display_amount(self):
        print("Amount: 1000")
class UPIPayment(Payment):
    def pay(self):
        print("Payment using UPI")
class CardPayment(Payment):
    def pay(self):
        print("Payment using Card")
u = UPIPayment()
c = CardPayment()
u.pay()
u.display_amount()
c.pay()
c.display_amount()