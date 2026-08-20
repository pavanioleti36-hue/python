class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Grade: " + self.grade)
        print("-" * 20)


student1 = Student("Ananya", 20, "A")
student2 = Student("Rahul", 22, "B")

student1.display()
student2.display()
