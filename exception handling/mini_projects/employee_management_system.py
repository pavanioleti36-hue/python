class InvalidEmployeeIDError(Exception): pass
class InvalidSalaryError(Exception): pass
class InvalidDepartmentError(Exception): pass
class EmployeeManagement:
    def __init__(self):
        self.employees = {}
        self.departments = ["IT", "HR", "Finance"]
    def add_employee(self, emp_id, name, salary, department):
        try:
            if emp_id <= 0 or emp_id in self.employees:
                raise InvalidEmployeeIDError("Invalid or duplicate employee ID")
            if salary < 0:
                raise InvalidSalaryError("Salary cannot be negative")
            if department not in self.departments:
                raise InvalidDepartmentError("Invalid department")
            self.employees[emp_id] = {"name": name, "salary": salary, "department": department}
            print("Employee added")
        except (InvalidEmployeeIDError, InvalidSalaryError, InvalidDepartmentError) as e:
            print(e)
system = EmployeeManagement()
system.add_employee(1, "Anu", 30000, "IT")
system.add_employee(2, "Ravi", -5000, "Sales")