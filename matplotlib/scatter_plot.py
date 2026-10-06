import matplotlib.pyplot as plt
hours= [1, 2, 3, 4, 5, 6, 7, 8]
marks= [35, 42, 45, 48, 51, 55, 58, 61]
plt.scatter(hours, marks)
plt.title("Scatter Plot of Hours vs Marks")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.show()