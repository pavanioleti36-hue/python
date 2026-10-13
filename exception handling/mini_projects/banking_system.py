class InvalidAccountError(Exception): pass
class InsufficientBalanceError(Exception): pass
class InvalidAmountError(Exception): pass
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    def withdraw(self, account_no, amount):
        try:
            if account_no != self.account_no:
                raise InvalidAccountError("Invalid account number")
            if amount <= 0:
                raise InvalidAmountError("Amount must be positive")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
            self.balance -= amount
            print("Remaining balance:", self.balance)
        except (InvalidAccountError, InvalidAmountError, InsufficientBalanceError) as e:
            print(e)
account = BankAccount("12345", 5000)
account.withdraw("12345", 23425)