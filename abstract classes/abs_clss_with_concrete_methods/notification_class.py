from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
    def display_message(self):
        print("Message: Hello")
class Email(Notification):
    def send(self):
        print("Email sent")
class SMS(Notification):
    def send(self):
        print("SMS sent")
e = Email()
s = SMS()
e.send()
e.display_message()
s.send()
s.display_message()