class Book:
    def __init__(self, title):
        self.title = title
    def display(self):
        print("Book:", self.title)
class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("SQL")
        ]
    def show_books(self):
        for book in self.books:
            book.display()
library = Library()
library.show_books()