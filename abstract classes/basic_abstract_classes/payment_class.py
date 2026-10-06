from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPTpayment(Payment):
    def pay(self):
        print("Payment made through UPI")
class CardPayment(Payment):
    def pay(self):
        print("Payment made through Card")
u= UPTpayment()
c= CardPayment()
u.pay() 
c.pay()