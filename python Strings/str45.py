courses = """
Python Programming
Java Full Stack
Data Science
Data Analysis
Digital Marketing
"""
search = input("Search Course: ").strip().lower()
if search in courses.lower():
    print("Course Available")
else:
    print("Course Not Available")


#message
student_name = "Ravi"
course_name = "Python Programming"
message = f"""
Hello {student_name},
Welcome to the {course_name} training program.
Your classes start from tomorrow.
Thank you.
"""
print(message)

#code generate
product_name = "cycle"
product_id = 213
code = (
product_name[:3].upper()
+ "-"
+ str(product_id).zfill(4)
)
print(code)