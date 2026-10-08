from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration
    @abstractmethod
    def mode(self):
        pass
class OnlineCourse(Course):
    def mode(self):
        print("Online Course")
class OfflineCourse(Course):
    def mode(self):
        print("Offline Course")
OnlineCourse("Python", 3).mode()
OfflineCourse("Java", 4).mode()