class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def study(self):
        print(self.name,"is studying")
class Teacher(Person):
    def teach(self):
        print(self.name,"is teaching")
class NotificationService:
    def send(self,message):
        print("Notification:",message)
class School:
    def __init__(self):
        self.students=[Student("Pavani"),Student("Ravi")]
        self.teachers=[Teacher("Anu")]
    def notify(self,service):
        service.send("School meeting tomorrow")
school=School()
school.students[0].study()
school.teachers[0].teach()
school.notify(NotificationService())