class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return "Deposited: " + str(amount) + " | Current Balance: " + str(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal denied! Insufficient balance."
        else:
            self.balance -= amount
            return "Withdrawn: " + str(amount) + " | Current Balance: " + str(self.balance)

acc1 = BankAccount("Ananya", 5000)

print(acc1.deposit(2000))
print(acc1.withdraw(3000))
print(acc1.withdraw(5000)) 
