import matplotlib.pyplot as plt
marks= [85, 90, 78, 92, 88]
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
plt.pie(marks, labels=students)
plt.title("Student Marks Distribution")
plt.show()