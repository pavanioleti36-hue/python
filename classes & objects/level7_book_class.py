class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

    def issue_book(self):
        if self.is_issued:
            return "Book '" + self.title + "' is already issued."
        else:
            self.is_issued = True
            return "Book '" + self.title + "' has been issued."

    def return_book(self):
        if not self.is_issued:
            return "Book '" + self.title + "' was not issued."
        else:
            self.is_issued = False
            return "Book '" + self.title + "' has been returned."


# Example usage
book1 = LibraryBook("Python Programming")
book2 = LibraryBook("Data Science Handbook")

print(book1.issue_book())
print(book1.issue_book())   
print(book1.return_book())
print(book1.return_book())  
