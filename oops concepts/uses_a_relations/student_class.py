class Printer:
    def print_details(self, name, roll_no):
        print("Student Name:", name)
        print("Roll No:", roll_no)


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_details(self, printer):
        printer.print_details(self.name, self.roll_no)


student = Student("Pavani", 101)
printer = Printer()

student.show_details(printer)