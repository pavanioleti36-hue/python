class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")
class UPI:
    def pay(self):
        print("Payment made using UPI")
class Cash:
    def pay(self):
        print("Payment made using Cash")
def process_payment(payment):
    payment.pay()
credit = CreditCard()
upi = UPI()
cash = Cash()
process_payment(credit)
process_payment(upi)
process_payment(cash)