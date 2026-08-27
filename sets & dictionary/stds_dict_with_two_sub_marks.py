subject1 = {
    "pavani": 85,
    "Ravi": 78,
    "Anusha": 92,
    "Manoj": 67
}
subject2 = {
    "Divya": 88,
    "Ravi": 82,
    "Anusha": 90,
    "Arun": 75,
    "pavani":98
}
common_students = set(subject1.keys()) & set(subject2.keys())
print("Students appearing in both subjects:")
for student in common_students:
    print(student)