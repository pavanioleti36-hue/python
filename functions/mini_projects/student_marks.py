students = {}
def add_student():
    name = input("Enter student name: ")
    students[name] = float(input("Enter marks: "))
def search_student():
    name = input("Enter student name: ")
    print(name, students.get(name, "Student not found"))
def update_student():
    name = input("Enter student name: ")
    if name in students:
        students[name] = float(input("Enter new marks: "))
    else:
        print("Student not found")
def delete_student():
    name = input("Enter student name: ")
    print("Deleted" if students.pop(name, None) is not None else "Student not found")
def display_students():
    print(students if students else "No students available")
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        break
    else:
        print("Invalid choice")