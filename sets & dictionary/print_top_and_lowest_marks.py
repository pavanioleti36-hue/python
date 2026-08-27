marks = {
    "Pavani": 85,
    "Ravi": 78,
    "Anusha": 92,
    "Manoj": 97,
    "priya": 58
}

topper = None
top_marks = -1
lowest = None
low_marks = 9999

for student, score in marks.items():
    if score > top_marks:
        top_marks = score
        topper = student
    if score < low_marks:
        low_marks = score
        lowest = student

print("Topper:", topper, "with marks:", top_marks)
print("Lowest scorer:", lowest, "with marks:", low_marks)
