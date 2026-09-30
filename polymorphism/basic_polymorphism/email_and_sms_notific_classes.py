class emailnotification:
    def send(self):
        print("Email notification sent")
class smsnotification:
    def send(self):
        print("SMS notification sent")
en= emailnotification()
sn= smsnotification()
en.send()
sn.send()