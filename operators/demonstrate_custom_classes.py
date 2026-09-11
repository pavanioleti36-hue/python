class Student:
    def __init__(self, name):
        self.name = name
student1 = Student("Pavani")
student2 = Student("Pavani")
student3 = student1
print(student1 is student2)
print(student1 is student3)