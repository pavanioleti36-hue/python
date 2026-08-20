class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        print("Student: " + self.name)
        print("Marks: " + str(self.marks))
        print("Total Marks: " + str(self.total_marks()))
        print("Average Marks: " + str(self.average_marks()))


student1 = Student("Rahul", [85, 90, 78, 92])
student2 = Student("Priya", [70, 88, 95, 80])
student3 = Student("Arjun", [60, 75, 68, 72])

student1.display_info()
student2.display_info()
student3.display_info()
