class student:
    college= "aditya college"
    def __init__(self,name):
        self.name= name
    def display(self):
        print("Student Name:", self.name)
        print("College Name:", student.college)
stu1= student("pavani")
stu2= student("prasad")            
stu1.display()
stu2.display()