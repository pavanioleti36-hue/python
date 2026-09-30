class notification:
    def send(self):
        print("notification is send")
class email(notification):
    def send(self):
        print("notification is send through email")
class sms(notification):
    def send(self):
        print("notification is send through sms")
class whatsapp(notification):
    def send(self):
        print("notification is send through whatsapp")
e= email()
s= sms()
w= whatsapp()
e.send()
s.send()
w.send()