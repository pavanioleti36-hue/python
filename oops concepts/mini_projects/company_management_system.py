class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Developer(Employee):
    def code(self):
        print(self.name,"writes code")
class Manager(Employee):
    def manage(self):
        print(self.name,"manages team")
class Department:
    def __init__(self,name):
        self.name=name
class PayrollService:
    def pay(self,employee):
        print("Salary paid to",employee.name)
class Company:
    def __init__(self):
        self.departments=[Department("IT"),Department("HR")]
        self.employees=[Developer("Pavani",40000),Manager("Ravi",50000)]
    def payroll(self,service):
        for employee in self.employees:
            service.pay(employee)
company=Company()
company.employees[0].code()
company.employees[1].manage()
company.payroll(PayrollService())