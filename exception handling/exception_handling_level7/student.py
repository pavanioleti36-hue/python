class InvalidMarksError(Exception):
    pass
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        try:
            if self.marks < 0 or self.marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100")
            print(self.name, self.marks)
        except InvalidMarksError as e:
            print(e)
student = Student("Ravi", 110)
student.display()