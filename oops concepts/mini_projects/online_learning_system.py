class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def study(self):
        print(self.name,"is studying")
class Teacher(Person):
    def teach(self):
        print(self.name,"is teaching")
class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
class NotificationService:
    def send(self,message):
        print("Notification:",message)
class CertificateService:
    def generate(self,student,course):
        print("Certificate for",student.name,"in",course.name)
student=Student("Pavani")
teacher=Teacher("Ravi")
course=Course("Python")
course.add_student(student)
student.study()
teacher.teach()
NotificationService().send("Course completed")
CertificateService().generate(student,course)