class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Student:", self.name)
class College:
    def __init__(self):
        self.students = [
            Student("Pavani"),
            Student("Ravi"),
            Student("Anu")
        ]
    def show_students(self):
        for student in self.students:
            student.display()
college = College()
college.show_students()