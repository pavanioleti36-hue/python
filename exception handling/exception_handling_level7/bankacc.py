class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
            self.balance -= amount
            print("Remaining balance:", self.balance)
        except (ValueError, InsufficientBalanceError) as e:
            print(e)
account = BankAccount(5000)
account.withdraw(6000)