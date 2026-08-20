class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Course: " + self.course)
        print("Marks: " + str(self.marks))


student1 = Student("Rahul", 20, "Computer Science", 85)
student2 = Student("Priya", 19, "Data Science", 90)
student3 = Student("Arjun", 21, "Business Management", 78)

student1.display_info()
print()
student2.display_info()
print()
student3.display_info()
