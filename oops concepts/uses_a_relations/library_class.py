class SearchService:
    def search(self, book_name):
        print("Searching for:", book_name)


class Library:
    def __init__(self, name):
        self.name = name

    def search_book(self, service, book_name):
        service.search(book_name)


library = Library("City Library")
search_service = SearchService()

library.search_book(search_service, "Python Programming")