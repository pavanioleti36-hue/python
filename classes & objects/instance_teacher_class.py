class teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
    def display(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")
teacher1 = teacher("bhaskar", "Maths", 10)
teacher2 = teacher("asha", "Science", 8)
teacher3 = teacher("nandhini", "English", 12)        
teacher1.display()
teacher2.display()
teacher3.display()