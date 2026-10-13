class InvalidBookIDError(Exception): pass
class BookUnavailableError(Exception): pass
class DuplicateBookError(Exception): pass
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, book_id, title):
        try:
            if book_id <= 0:
                raise InvalidBookIDError("Invalid book ID")
            if book_id in self.books:
                raise DuplicateBookError("Book already exists")
            self.books[book_id] = {"title": title, "available": True}
            print("Book added")
        except (InvalidBookIDError, DuplicateBookError) as e:
            print(e)
    def borrow_book(self, book_id):
        try:
            if book_id not in self.books:
                raise InvalidBookIDError("Invalid book ID")
            if not self.books[book_id]["available"]:
                raise BookUnavailableError("Book is unavailable")
            self.books[book_id]["available"] = False
            print("Book borrowed:", self.books[book_id]["title"])
        except (InvalidBookIDError, BookUnavailableError) as e:
            print(e)
library = Library()
library.add_book(1, "Python")
library.add_book(1, "Java")
library.borrow_book(1)
library.borrow_book(1)