from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number
    @abstractmethod
    def calculate_interest(self):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 5000 * 0.04
a = SavingsAccount("Pavani", 12345)
print(a.holder, a.account_number, a.calculate_interest())