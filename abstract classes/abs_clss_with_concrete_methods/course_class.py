from abc import ABC, abstractmethod
class Course(ABC):
    @abstractmethod
    def start(self):
        pass
    def display_course_details(self):
        print("Course: Python Programming")
class OnlineCourse(Course):
    def start(self):
        print("Online course started")
class OfflineCourse(Course):
    def start(self):
        print("Offline course started")
o = OnlineCourse()
f = OfflineCourse()
o.start()
o.display_course_details()
f.start()
f.display_course_details()