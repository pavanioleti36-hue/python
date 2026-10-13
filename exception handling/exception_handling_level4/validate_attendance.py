attendance = float(input("Enter attendance percentage: "))
try:
    if attendance < 75:
        raise ValueError("Attendance must be at least 75%")
    print("Eligible for exams")
except ValueError as e:
    print(e)