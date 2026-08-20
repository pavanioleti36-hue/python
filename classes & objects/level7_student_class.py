class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def get_info(self):
        return "Name: " + self.name

    @classmethod
    def total_students(cls):
        return cls.count


s1 = Student("Ananya")
s2 = Student("Rahul")
s3 = Student("Pavani")

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())
print("Total students created: " + str(Student.total_students()))
