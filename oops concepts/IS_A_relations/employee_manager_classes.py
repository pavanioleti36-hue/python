class employee:
    def work(self):
        print("employee works in company")
class manager(employee):
    def name(self):
        print("manager is an employee")
c= manager()
c.work()
c.name()