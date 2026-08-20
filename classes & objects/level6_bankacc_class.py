class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

bankacc = BankAccount()
print(bankacc.deposit(20030))
print("present balance:", bankacc.balance)       