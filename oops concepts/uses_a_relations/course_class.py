class Certificate:
    def generate(self, name, course):
        print("Certificate")
        print("Name:", name)
        print("Course:", course)
class course:
    def __init__(self, name):
        self.name = name

    def issue_certificate(self, certificate, student_name):
        certificate.generate(student_name, self.name)
c= course("Python Programming")
cer= Certificate()
c.issue_certificate(cer, "Pavani")