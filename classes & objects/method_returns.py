class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return "Name: " + self.name + ", Grade: " + str(self.grade)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def student_info(self, student_obj):
        return "Teacher: " + self.name + ", Subject: " + self.subject + " → " + student_obj.get_info()


# Example usage
s1 = Student("Ananya", "A")
s2 = Student("Rahul", "B")

t1 = Teacher("Mr. Sharma", "Math")

print(t1.student_info(s1))
print(t1.student_info(s2))
