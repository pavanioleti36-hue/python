class BookNotAvailableError(Exception):
    pass
class Library:
    def __init__(self, books):
        self.books = books
    def borrow(self, book):
        try:
            if book not in self.books:
                raise BookNotAvailableError("Book is not available")
            self.books.remove(book)
            print("Borrowed:", book)
        except BookNotAvailableError as e:
            print(e)
library = Library(["Python", "Java", "C++"])
library.borrow("HTML")