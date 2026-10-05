class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def study(self):
        print("Student is studying")
class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")
s = Student("Pavani", 20)
t = Teacher("Ravi", 35)
s.display()
s.study()
t.display()
t.teach()