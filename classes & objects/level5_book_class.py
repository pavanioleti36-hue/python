class Book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price

    def display_info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Publisher: " + self.publisher)
        print("Price: " + str(self.price))


book1 = Book("Python Programming", "John Smith", "TechPress", 550)
book2 = Book("Data Science Essentials", "Priya Sharma", "EduWorld", 750)
book3 = Book("Machine Learning Basics", "Arjun Kumar", "AI Publishers", 900)

book1.display_info()
print()
book2.display_info()
print()
book3.display_info()
