class  emailservice:
    def send(self):
        print("email servicing")
class smsservice:
    def send(self):
        print("sms servicing")
def obj_cls(obj):
    obj.send()
email= emailservice()
sms= smsservice()
obj_cls(email)
obj_cls(sms)                    