sub1= int(input("Enter the subject 1 marks: "))
sub2= int(input("Enter the subject 2 marks: "))
sub3= int(input("Enter the subject 3 marks: "))
total_marks= sub1 + sub2 + sub3
avg= total_marks / 3
percentage= (total_marks / 300) * 100
if percentage >=90:
    grade= "A+"
elif percentage >=80:
    grade= "A"
elif percentage >=70:
    grade= "B"
elif percentage >=60:
    grade= "C"
elif percentage >=50:
    grade= "D"
elif percentage >=35:
    grade= "E" 
else:
    grade= "F"

if (sub1>=35) and (sub2>=35) and (sub3>=35):
    status= "Pass"
else:
    status= "Fail"

print("The total marks of the student is: ", total_marks)
print("The average marks of the student is: ", avg)
print("The percentage of the student is: ", percentage)
print("The grade of the student is: ", grade)
print("The status of the student is: ", status)                               