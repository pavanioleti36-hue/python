class Manager:
    def work(self):
        print("Manager manages the team")
class Developer:
    def work(self):
        print("Developer writes code")
class Tester:
    def work(self):
        print("Tester tests the application")
def assign_work(employee):
    employee.work()
manager = Manager()
developer = Developer()
tester = Tester()
assign_work(manager)
assign_work(developer)
assign_work(tester)