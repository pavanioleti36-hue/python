class upipayment:
    def pay(self):
        print("Payment done using UPI")
class cardpayment:  
    def pay(self):
        print("Payment done using card")
class  cashpayment:
    def pay(self):
        print("Payment done using cash")
u= upipayment()
c= cardpayment()
cash= cashpayment()
u.pay()
c.pay()
cash.pay()