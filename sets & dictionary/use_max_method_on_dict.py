marks = {"Pavani": 98, "Ravi": 78, "ramani": 92, "Manoj": 67, "Divya": 88}
top = None
maxm = -1
for s, m in marks.items():
    if m > maxm:
        maxm = m
        top = s
print("Topper:", top, "with marks:", maxm)