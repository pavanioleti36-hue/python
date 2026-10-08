from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    @abstractmethod
    def display(self):
        pass
class SavingsAccount(Account):
    def display(self):
        print("Savings Account:", self.account_number, self.balance)
class CurrentAccount(Account):
    def display(self):
        print("Current Account:", self.account_number, self.balance)
SavingsAccount(101, 50000).display()
CurrentAccount(102, 100000).display()