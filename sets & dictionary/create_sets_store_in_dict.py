set1 = {"Pavani", "Ravi", "Anusha"}
set2 = {"Manoj", "Divya"}
courses = {
    "Pavani": "Computer Science",
    "Ravi": "Mechanical",
    "Anusha": "Electronics",
    "Manoj": "Civil",
    "Divya": "IT"
}
print("Students in Set 1 and their courses:")
for student in set1:
    print(student + " - " + courses[student])
print("\nStudents in Set 2 and their courses:")
for student in set2:
    print(student + " - " + courses[student])