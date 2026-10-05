class Book:
    def __init__(self,title):
        self.title=title
    def show(self):
        print("Book:",self.title)
class EBook(Book):
    def download(self):
        print("Downloading:",self.title)
class SearchService:
    def search(self,name):
        print("Searching:",name)
class Library:
    def __init__(self):
        self.books=[Book("Python"),EBook("Java")]
    def search_book(self,service,name):
        service.search(name)
library=Library()
library.books[1].download()
library.search_book(SearchService(),"Python")