class Email:
    def send(self, message):
        print("Email:", message)
class SMS:
    def send(self, message):
        print("SMS:", message)
class WhatsApp:
    def send(self, message):
        print("WhatsApp:", message)
notifications = [Email(), SMS(), WhatsApp()]
for notification in notifications:
    notification.send("Your order has been shipped")