students = [
    ("Ravi", 85),
    ("Anusha", 78),
    ("Kavya", 92),
    ("Meera", 69),
    ("Pavani", 98)
]

search_name = "Pavani"

found = False
for name, marks in students:
    if name == search_name:
        print("Student found → Name:", name, "Marks:", marks)
        found = True
        break

if not found:
    print("Student not found")
