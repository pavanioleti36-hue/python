from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class UPIPayment(Payment):
    def pay(self):
        print("Paid", self.amount, "using UPI")

    def refund(self):
        print("Refunded", self.amount, "through UPI")

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid", self.amount, "using Credit Card")

    def refund(self):
        print("Refunded", self.amount, "to Credit Card")

class DebitCardPayment(Payment):
    def pay(self):
        print("Paid", self.amount, "using Debit Card")

    def refund(self):
        print("Refunded", self.amount, "to Debit Card")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid", self.amount, "using Net Banking")

    def refund(self):
        print("Refunded", self.amount, "through Net Banking")

payments = [
    UPIPayment(1000),
    CreditCardPayment(2000),
    DebitCardPayment(1500),
    NetBankingPayment(3000)
]

for payment in payments:
    payment.pay()
    payment.refund()