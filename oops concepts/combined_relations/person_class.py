class Person:
    def show_person(self):
        print("This is a person")
class Course:
    def __init__(self, name):
        self.name = name
    def show_course(self):
        print("Course:", self.name)
class Student(Person):
    def __init__(self, name):
        self.name = name
        self.course = Course("Python")
    def show_student(self):
        print("Student:", self.name)
        self.course.show_course()
student = Student("Pavani")
student.show_person()
student.show_student()