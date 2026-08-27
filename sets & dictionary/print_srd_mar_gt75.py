students = {
    "Pavani": 85,
    "Rahul": 72,
    "Sita": 90,
    "Ravi": 68,
    "Anu": 78
}
print("Students who scored above 75:")
for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)