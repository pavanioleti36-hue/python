books = {}
def add_book():
    name = input("Enter book title: ")
    books[name] = books.get(name, 0) + 1
def search_book():
    name = input("Enter book title: ")
    print("Available copies:", books.get(name, 0))
def issue_book():
    name = input("Enter book title: ")
    if books.get(name, 0) > 0:
        books[name] -= 1
        print("Book issued")
    else:
        print("Book not available")
def return_book():
    name = input("Enter book title: ")
    books[name] = books.get(name, 0) + 1
    print("Book returned")
def display_books():
    available = {name: count for name, count in books.items() if count > 0}
    print(available if available else "No books available")
while True:
    print("\n1.Add 2.Search 3.Issue 4.Return 5.Display Available 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice")