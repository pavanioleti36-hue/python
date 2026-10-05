class ReportGenerator:
    def generate(self, name, salary):
        print("Employee Report")
        print("Name:", name)
        print("Salary:", salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def create_report(self, report_generator):
        report_generator.generate(self.name, self.salary)


employee = Employee("Ravi", 40000)
report = ReportGenerator()

employee.create_report(report)