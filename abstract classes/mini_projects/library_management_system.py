from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self.borrowed = False

    @abstractmethod
    def display_info(self):
        pass

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(self.title, "borrowed successfully")
        else:
            print(self.title, "is already borrowed")

    def return_item(self):
        self.borrowed = False
        print(self.title, "returned successfully")

class Book(LibraryItem):
    def display_info(self):
        print("Book:", self.title)

class Magazine(LibraryItem):
    def display_info(self):
        print("Magazine:", self.title)

class Newspaper(LibraryItem):
    def display_info(self):
        print("Newspaper:", self.title)

items = [
    Book("Python Programming"),
    Magazine("Technology Today"),
    Newspaper("Daily News")
]

for item in items:
    item.display_info()
    item.borrow()
    item.return_item()
    print()