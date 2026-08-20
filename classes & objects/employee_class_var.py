class employee:
    company_name= "Anurag IT solutions"
    employee_count= 0
    def __init__(self, name):
        self.name= name
        employee.employee_count += 1
    def display(self):
        print("Employee Name:", self.name)
        print("Company Name:", employee.company_name)
emp1= employee("pavani")
emp2= employee("prasanna")    
emp3= employee("sushma")
emp4= employee("rupa")
emp5= employee("sai")   
emp1.display()
emp2.display()
emp3.display()
emp4.display()
emp5.display()    
print("*"*30)
print("employee count:",employee.employee_count)     