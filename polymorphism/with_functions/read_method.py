class student:
    def read(self):
        print("Student reads the book")
class teacher:
    def read(self):
        print("Teacher reads the lesson")
class doctor:
    def read(self):
        print("Doctor reads the medical journal")
def assign_read(employee):
    employee.read()
student = student()
teacher = teacher()
doctor = doctor()
assign_read(student)
assign_read(teacher)
assign_read(doctor)