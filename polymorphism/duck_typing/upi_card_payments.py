class  upipayment:
    def pay(self):
        print("payment is done using upi method")
class cardpayment:
    def pay(self):
        print("payment is done using card")
def obj_cls(obj):
    obj.pay()
upi= upipayment()
card= cardpayment()
obj_cls(upi)
obj_cls(card)                    