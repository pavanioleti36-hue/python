class InvalidMarksError(Exception): pass
class DuplicateStudentError(Exception): pass
class StudentNotFoundError(Exception): pass
class StudentManagement:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, marks):
        try:
            if not 0 <= marks <= 100:
                raise InvalidMarksError("Marks must be between 0 and 100")
            if student_id in self.students:
                raise DuplicateStudentError("Student ID already exists")
            self.students[student_id] = {"name": name, "marks": marks}
            print("Student added")
        except (InvalidMarksError, DuplicateStudentError) as e:
            print(e)
    def show_student(self, student_id):
        try:
            if student_id not in self.students:
                raise StudentNotFoundError("Student not found")
            print(self.students[student_id])
        except StudentNotFoundError as e:
            print(e)
system = StudentManagement()
system.add_student(1, "Ravi", 85)
system.add_student(1, "Anu", 90)
system.show_student(2)