students = [
    ["Ravi", [85, 78, 92]],
    ["Anusha", [75, 88, 69]],
    ["Kiran", [90, 82, 87]],
    ["Meera", [65, 70, 72]],
    ["Pavani", [88, 95, 91]]
]

for student in students:   
    name = student[0]      
    marks = student[1]     
    total = sum(marks)    
    average = total / len(marks) 
    print("Name:", name, "Total:", total, "Average:", average)
