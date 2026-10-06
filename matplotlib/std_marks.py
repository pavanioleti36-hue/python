import matplotlib.pyplot as plt
marks= [35, 42, 45, 48, 51, 55, 58, 61, 65, 67, 72, 75, 78, 81, 85, 88, 91, 95]
plt.hist(marks, bins=6, edgecolor='black')
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()