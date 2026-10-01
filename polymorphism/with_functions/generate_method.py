class medicalreport:
    def generate(self):
        print("Medical report generated")
class schoolreport:
    def generate(self):
        print("School report generated")
class financialreport:
    def generate(self):
        print("Financial report generated")
def assign_generate(employee):
    employee.generate()
medical = medicalreport()
school = schoolreport()
financial = financialreport()
assign_generate(medical)
assign_generate(school)
assign_generate(financial)