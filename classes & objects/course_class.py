class course:
    institute_name= "Anurag IT solutions"
    def __init__(self, course_name, duration):
        self.course_name= course_name
        self.duration= duration
    def display(self):
      print("institute name:",course.institute_name)
      print("course name:",self.course_name)
      print("duration:",self.duration)
crs1= course("python", "6 months")
crs2= course("java", "12 months")
crs1.display()
crs2.display()