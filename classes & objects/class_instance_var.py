class Employee:
    company_name = "Tech Solutions Pvt Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name: " + self.name)
        print("Salary: " + str(self.salary))
        print("Company: " + Employee.company_name)
        print("-" * 25)


emp1 = Employee("Ananya", 50000)
emp2 = Employee("Rahul", 60000)

emp1.display_info()
emp2.display_info()

Employee.company_name = "Global Tech Ltd"

emp1.display_info()
emp2.display_info()
