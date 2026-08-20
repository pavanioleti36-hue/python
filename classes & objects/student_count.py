class std_count:
    count= 0
    def __init__(self, name):
        self.name = name
        std_count.count += 1
    def display(self):
        print("Student Name:", self.name)
std1 = std_count("pavani")
std2 = std_count("sai")
std1.display()  
std2.display()
print("Total Students:", std_count.count)