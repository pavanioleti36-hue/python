salaries = {"Arun": 35000, "Pavani": 42000, "Ravi": 28000, "Divya": 50000, "Manoj": 39000}
total = 0
count = 0
for s, sal in salaries.items():
    total += sal
    count += 1
avg = total / count
print("Average salary: " + str(avg))