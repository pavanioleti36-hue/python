std_marks= int(input("Enter the marks of the student: "))
marks_percentage= float(input("Enter the marks percentage of the student: "))
attendance_percentage= float(input("Enter the attendance percentage of the student: "))
req_marks= std_marks + 10  #extra marks for eligibility
if (marks_percentage >= 75) and (attendance_percentage >= 75) and (req_marks>= 70):
    print("The student is eligible for the scholarship.")
else:
    print("The student is not eligible for the scholarship.")    