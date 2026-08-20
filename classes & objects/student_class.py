class Student:
    college_name = "ABC Engineering College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print("Name: " + self.name)
        print("Roll No: " + str(self.roll_no))
        print("College: " + Student.college_name)
        print("-" * 25)

student1 = Student("Ananya", 101)
student2 = Student("Rahul", 102)
student3 = Student("Pavani", 103)
student1.display_info()
student2.display_info()
student3.display_info()
