from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def calculate_fee(self):
        pass

    def start_course(self):
        print("Course started:", self.name)
        print("Duration:", self.duration)

class ProgrammingCourse(Course):
    def calculate_fee(self):
        return 5000

class DataScienceCourse(Course):
    def calculate_fee(self):
        return 8000

class WebDevelopmentCourse(Course):
    def calculate_fee(self):
        return 6000

courses = [
    ProgrammingCourse("Python Programming", "3 Months"),
    DataScienceCourse("Data Science", "6 Months"),
    WebDevelopmentCourse("Web Development", "4 Months")
]

for course in courses:
    course.start_course()
    print("Course Fee:", course.calculate_fee())
    print()