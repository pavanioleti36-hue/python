def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 35:
        return "D"
    return "F"
def pass_fail(marks):
    return "Pass" if marks and all(mark >= 35 for mark in marks) else "Fail"
def find_topper(students):
    return max(students, key=lambda name: calculate_average(students[name])) if students else "No students"
students = {}
count = int(input("Enter number of students: "))
for _ in range(count):
    name = input("Enter student name: ")
    marks = [float(x) for x in input("Enter marks separated by spaces: ").split()]
    students[name] = marks
    average = calculate_average(marks)
    print("Total:", calculate_total(marks))
    print("Average:", average)
    print("Grade:", calculate_grade(average))
    print("Status:", pass_fail(marks))
print("Topper:", find_topper(students))