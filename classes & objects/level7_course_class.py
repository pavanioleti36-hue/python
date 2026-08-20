class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)
        return student_name + " has been enrolled in " + self.course_name

    def display_students(self):
        if not self.students:
            return "No students enrolled in " + self.course_name
        result = "Students enrolled in " + self.course_name + ":\n"
        for student in self.students:
            result += "- " + student + "\n"
        return result


# Example usage
course1 = Course("Python fullstack")

print(course1.enroll_student("suma"))
print(course1.enroll_student("pravee"))
print(course1.enroll_student("Pavani"))

print(course1.display_students())
