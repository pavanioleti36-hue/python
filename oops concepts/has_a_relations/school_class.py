class Teacher:
    def teach(self):
        print("Teacher is teaching")
class Student:
    def study(self):
        print("Student is studying")
class School:
    def __init__(self):
        self.teacher = Teacher()
        self.students = [
            Student(),
            Student()
        ]
    def conduct_class(self):
        self.teacher.teach()
        for student in self.students:
            student.study()
school = School()
school.conduct_class()