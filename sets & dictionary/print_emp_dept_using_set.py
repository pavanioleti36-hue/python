employees = {
    "Pavani": "cse",
    "Ravi": "mech",
    "Anusha": "ece",
    "Manoj": "civil",
    "Divya": "IT",
    "Arun": "cse"
}
unique_departments = set(employees.values())
print("Unique departments:")
for dept in unique_departments:
    print(dept)