class Employee:
    company_name = "Anurag IT Solutions Pvt Ltd"

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print("Name: " + self.name)
        print("Employee ID: " + str(self.emp_id))
        print("Company: " + Employee.company_name)
        print("-" * 25)


# Creating multiple Employee objects
emp1 = Employee("suma", 201)
emp2 = Employee("pravee", 202)
emp3 = Employee("Pavani", 203)

# Displaying their information
emp1.display_info()
emp2.display_info()
emp3.display_info()
