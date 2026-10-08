from abc import ABC, abstractmethod
class UniversityCourse(ABC):
    @abstractmethod
    def start_course(self):
        pass
class Engineering(UniversityCourse):
    def start_course(self):
        print("Engineering course started")
class Medical(UniversityCourse):
    def start_course(self):
        print("Medical course started")
class Management(UniversityCourse):
    def start_course(self):
        print("Management course started")
courses = [Engineering(), Medical(), Management()]
for course in courses:
    course.start_course()