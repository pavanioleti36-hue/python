from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.04
        print("Savings Interest:", interest)

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.02
        print("Current Account Interest:", interest)

a1 = SavingsAccount("Pavani", "S101", 10000)
a2 = CurrentAccount("Manoj", "C101", 20000)

a1.deposit(2000)
a1.withdraw(1000)
a1.calculate_interest()
a1.display_balance()

print()

a2.deposit(5000)
a2.calculate_interest()
a2.display_balance()