class InvalidEnrollmentError(Exception):
    pass
class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.enrolled = 0
    def enroll(self):
        try:
            if self.enrolled >= self.capacity:
                raise InvalidEnrollmentError("Course is full")
            self.enrolled += 1
            print("Enrollment successful:", self.name)
        except InvalidEnrollmentError as e:
            print(e)
course = Course("Python", 1)
course.enroll()
course.enroll()