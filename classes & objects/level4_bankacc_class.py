class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")

account1 = BankAccount("Rahul", 5000)
account2 = BankAccount("Priya", 10000)

account1.display_info()
account1.deposit(2000)
account1.withdraw(3000)
account1.withdraw(5000)  

account2.display_info()
account2.deposit(5000)
account2.withdraw(12000)
