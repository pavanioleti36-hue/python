from abc import ABC, abstractmethod
class notification(ABC):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def receive(self):
        pass
class EmailNotification(notification):
    def send(self):
        print("Notification sent through Email")
    def receive(self):
        print("Notification received through Email")
class SMSNotification(notification):
    def send(self):
        print("Notification sent through SMS")
    def receive(self):
        print("Notification received through SMS")
e= EmailNotification()
s= SMSNotification()
e.send()
e.receive()
s.send()
s.receive()
