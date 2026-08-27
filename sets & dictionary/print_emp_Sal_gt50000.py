salaries = {
    "Arun": 48000,
    "Pavani": 62000,
    "Ravi": 55000,
    "Divya": 47000,
    "Manoj": 72000
}
print("Employees earning more than ₹50,000:")
for emp, sal in salaries.items():
    if sal > 50000:
        print(emp + " - " + str(sal))