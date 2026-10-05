class Department:
    def __init__(self, name):
        self.name = name
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class PayrollService:
    def process_salary(self, employee):
        print("Salary processed for", employee.name)
class Company:
    def __init__(self):
        self.departments = [Department("IT"), Department("HR")]
        self.employees = [Employee("Pavani", 40000), Employee("Ravi", 35000)]
    def process_payroll(self, payroll_service):
        for employee in self.employees:
            payroll_service.process_salary(employee)
company = Company()
payroll = PayrollService()
company.process_payroll(payroll)