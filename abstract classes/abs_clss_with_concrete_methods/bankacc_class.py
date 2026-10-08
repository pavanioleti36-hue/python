from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
    def display_balance(self):
        print("Balance: 10000")
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Interest: 5%")
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Interest: 2%")
s = SavingsAccount()
c = CurrentAccount()
s.calculate_interest()
s.display_balance()
c.calculate_interest()
c.display_balance()