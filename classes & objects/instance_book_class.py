class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def display_info(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)
        print("Pages: ", self.pages)
        

book1 = Book("Python Basics", "John Smith", 450, 300)
book2 = Book("Data Science Handbook", "Emily Davis", 800, 500)
book3 = Book("Machine Learning Guide", "Michael Brown", 1200, 650)

book1.display_info()
book2.display_info()
book3.display_info()
