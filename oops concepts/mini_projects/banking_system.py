class Account:
    def __init__(self,number,balance):
        self.number=number
        self.balance=balance
    def show_balance(self):
        print("Balance:",self.balance)
class SavingsAccount(Account):
    def interest(self):
        print("Savings account interest")
class Customer:
    def __init__(self,name):
        self.name=name
class PaymentService:
    def pay(self,amount):
        print("Payment:",amount)
class Bank:
    def __init__(self):
        self.customers=[Customer("Pavani"),Customer("Ravi")]
    def make_payment(self,service,amount):
        service.pay(amount)
account=SavingsAccount(101,10000)
account.show_balance()
account.interest()
bank=Bank()
bank.make_payment(PaymentService(),2000)