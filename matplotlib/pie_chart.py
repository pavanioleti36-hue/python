import matplotlib.pyplot as plt
courses= ['Python', 'Java', 'C++', 'JavaScript', 'SQL']
students= [120, 90, 60, 150, 80]
plt.pie(students, labels=courses, autopct='%1.1f%%')
plt.title("Distribution of Students in Different Courses")
plt.show()
