class EducationalInstitution:
    def conduct_education(self):
        print("Educational institution provides education")
class Department:
    def __init__(self, name):
        self.name = name
class ExaminationService:
    def conduct_exam(self):
        print("Examination conducted")
class University(EducationalInstitution):
    def __init__(self):
        self.departments = [Department("Computer Science"), Department("Mechanical")]
    def conduct_examination(self, examination_service):
        examination_service.conduct_exam()
university = University()
university.conduct_education()
exam_service = ExaminationService()
university.conduct_examination(exam_service)