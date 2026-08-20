class employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def display(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
emp1 = employee("bhaskar", "IT", 80000)
emp2 = employee("sai", "HR", 60000)
emp3 = employee("rupa", "Finance", 70000)
emp4 = employee("pavani", "Marketing", 75000)
emp5 = employee("asha", "Sales", 65000)
emp1.display()
emp2.display()
emp3.display()
emp4.display()
emp5.display()