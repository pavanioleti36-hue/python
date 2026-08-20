class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("-"*15)

student1 = Student("Ananya", 82)
student2 = Student("Rahul", 68)
student3 = Student("Pavani", 98)

student1.display_info()
student2.display_info()
student3.display_info()
