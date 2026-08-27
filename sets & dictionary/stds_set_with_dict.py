students = ["Pavani", "Ravi", "Anusha", "Ravi", "Divya", "Pavani", "Manoj", "Pavani"]
freq = {}
for name in students:
    if name in freq:
        freq[name] += 1
    else:
        freq[name] = 1
print("Student name frequencies:")
for student, count in freq.items():
    print(student + " - " + str(count))