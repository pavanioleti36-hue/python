class PaymentService:
    def make_payment(self, amount):
        print("Payment of", amount, "processed")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, payment_service, amount):
        if amount <= self.balance:
            payment_service.make_payment(amount)
            self.balance -= amount
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")


account = BankAccount(10000)
service = PaymentService()

account.pay(service, 3000)