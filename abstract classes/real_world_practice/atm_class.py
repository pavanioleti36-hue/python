from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class BankATM(ATM):
    def withdraw(self):
        print("Withdrawal successful")
    def deposit(self):
        print("Deposit successful")
    def check_balance(self):
        print("Balance: 10000")
atm = BankATM()
atm.withdraw()
atm.deposit()
atm.check_balance()