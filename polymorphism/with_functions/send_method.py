class Email:
    def send(self):
        print("Notification sent through Email")
class SMS:
    def send(self):
        print("Notification sent through SMS")
class WhatsApp:
    def send(self):
        print("Notification sent through WhatsApp")
def send_notification(notification):
    notification.send()
email = Email()
sms = SMS()
whatsapp = WhatsApp()
send_notification(email)
send_notification(sms)
send_notification(whatsapp)