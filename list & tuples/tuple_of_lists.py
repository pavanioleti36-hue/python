data = (
    ["Ravi", 85, 90],
    ["Anusha", 78, 88],
    ["Kiran", 92, 81]
)

print("Before modification:")
for student in data:
    print(student)

data[0][1] = 95
data[1][2] = 91
data[2][0] = "kavya"
print("\nAfter modification:")
for student in data:
    print(student)
