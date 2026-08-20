class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("City: " + self.city)

person1 = Person("Ananya", 25, "Hyderabad")
person2 = Person("Rahul", 30, "Bangalore")

# Displaying their information
person1.display_info()
person2.display_info()
