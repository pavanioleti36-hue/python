class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
student1 = student("pavani", 18, "csc")
student2 = student("rupa", 18, "Bipc")
student3 = student("sai", 18, "MPC")   
student1.display_info()     
student2.display_info()
student3.display_info()