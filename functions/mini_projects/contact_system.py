contacts = {}
def add_contact():
    name = input("Enter name: ")
    contacts[name] = input("Enter phone number: ")
def search_contact():
    name = input("Enter name: ")
    print(name, contacts.get(name, "Contact not found"))
def update_contact():
    name = input("Enter name: ")
    if name in contacts:
        contacts[name] = input("Enter new phone number: ")
    else:
        print("Contact not found")
def delete_contact():
    name = input("Enter name: ")
    print("Deleted" if contacts.pop(name, None) is not None else "Contact not found")
def display_contacts():
    print(contacts if contacts else "No contacts available")
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        break
    else:
        print("Invalid choice")