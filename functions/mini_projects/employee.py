employees = {}
def add_employee():
    name = input("Enter employee name: ")
    employees[name] = float(input("Enter salary: "))
def search_employee():
    name = input("Enter employee name: ")
    print(name, employees.get(name, "Employee not found"))
def update_employee():
    name = input("Enter employee name: ")
    if name in employees:
        employees[name] = float(input("Enter new salary: "))
    else:
        print("Employee not found")
def delete_employee():
    name = input("Enter employee name: ")
    print("Deleted" if employees.pop(name, None) is not None else "Employee not found")
def display_employees():
    print(employees if employees else "No employees available")
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        search_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        display_employees()
    elif choice == "6":
        break
    else:
        print("Invalid choice")