class  debitcard:
    def pay(self):
        print("payment made using debit card")
class creditcard:
    def pay(self):
        print("payment made using credit card")
def obj_cls(obj):
    obj.pay()
debit= debitcard()
credit= creditcard()
obj_cls(debit)
obj_cls(credit)                    