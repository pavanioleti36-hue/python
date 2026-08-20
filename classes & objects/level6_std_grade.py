class Student:
    def __init__(self, name):
        self.name = name

    def get_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

student1 = Student("Ananya")
student2 = Student("Rahul")
student3 = Student("Pavani")

print(student1.name, "Grade:", student1.get_grade(65))
print(student2.name, "Grade:", student2.get_grade(22))
print(student3.name, "Grade:", student3.get_grade(98))
