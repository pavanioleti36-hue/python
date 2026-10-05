class BankAccount:
    def deposit(self, amount):
        print("Deposited:", amount)
class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account provides interest")
class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current account provides overdraft facility")
s = SavingsAccount()
c = CurrentAccount()
s.deposit(5000)
s.interest()
c.deposit(10000)
c.overdraft()