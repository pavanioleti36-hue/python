class Teacher:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name
class NotificationService:
    def send(self, message):
        print("Notification:", message)
class School:
    def __init__(self):
        self.teachers = [Teacher("Anu"), Teacher("Ravi")]
        self.students = [Student("Pavani"), Student("Rahul")]
    def notify(self, notification_service):
        notification_service.send("School meeting tomorrow")
school = School()
notification = NotificationService()
school.notify(notification)