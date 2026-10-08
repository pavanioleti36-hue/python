from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Paid using UPI")
class Card(Payment):
    def pay(self):
        print("Paid using Card")
class NetBanking(Payment):
    def pay(self):
        print("Paid using Net Banking")
UPI(1000, "T101").pay()
Card(2000, "T102").pay()
NetBanking(3000, "T103").pay()