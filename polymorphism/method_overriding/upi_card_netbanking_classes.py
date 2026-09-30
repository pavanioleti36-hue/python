class payment:
    def pay(self):
        print("Amount payed")
class upi(payment):
    def pay(self):
        print("Amount payed by upi")
class creditcard(payment):
    def pay(self):
        print("Amount payed by credit card")
class netbanking(payment):
    def pay(self):
        print("Amount payed by netbanking")
u= upi()
c= creditcard()
net= netbanking()
u.pay()
c.pay()
net.pay()