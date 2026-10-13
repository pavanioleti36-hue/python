class InvalidPINError(Exception): pass
class InsufficientBalanceError(Exception): pass
class InvalidWithdrawalError(Exception): pass
class InvalidAccountError(Exception): pass
class ATM:
    def __init__(self, account_no, pin, balance):
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
    def withdraw(self, account_no, pin, amount):
        try:
            if account_no != self.account_no:
                raise InvalidAccountError("Invalid account")
            if pin != self.pin:
                raise InvalidPINError("Invalid PIN")
            if amount <= 0:
                raise InvalidWithdrawalError("Withdrawal amount must be positive")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
            self.balance -= amount
            print("Withdrawal successful. Balance:", self.balance)
        except (InvalidAccountError, InvalidPINError, InvalidWithdrawalError, InsufficientBalanceError) as e:
            print(e)
atm = ATM("12345", "2468", 5000)
atm.withdraw("12345", "2468", 1000)