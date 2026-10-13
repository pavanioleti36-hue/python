def topper(marks):
    return max(marks, key=marks.get)
students = {"Pavani": 95, "Ravi": 85, "Priya": 90}
print(topper(students))