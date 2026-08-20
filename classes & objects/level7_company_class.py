class Company:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, emp_id, emp_name):
        if emp_id in self.employees:
            return "Employee ID " + str(emp_id) + " already exists."
        self.employees[emp_id] = emp_name
        return emp_name + " has been added to " + self.name

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            removed = self.employees.pop(emp_id)
            return removed + " has been removed from " + self.name
        return "Employee ID " + str(emp_id) + " not found."

    def search_employee(self, emp_id):
        if emp_id in self.employees:
            return "Employee found: " + self.employees[emp_id]
        return "Employee ID " + str(emp_id) + " not found."

    def display_employees(self):
        if not self.employees:
            return "No employees in " + self.name
        result = "Employees in " + self.name + ":\n"
        for emp_id, emp_name in self.employees.items():
            result += str(emp_id) + " - " + emp_name + "\n"
        return result


# Example usage
company = Company("Tech Solutions Pvt Ltd")

print(company.add_employee(101, "Ananya"))
print(company.add_employee(102, "Rahul"))
print(company.add_employee(103, "Pavani"))

print(company.display_employees())

print(company.search_employee(102))
print(company.remove_employee(102))
print(company.display_employees())
