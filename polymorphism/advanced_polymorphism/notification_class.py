from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Email(Notification):
    def send(self):
        print("Sending Email Notification")
class SMS(Notification):
    def send(self):
        print("Sending SMS Notification")
class whatsapp(Notification):
    def send(self):
        print("Sending WhatsApp Notification")
e= Email()
s = SMS()
w = whatsapp()
e.send()
s.send()
w.send()