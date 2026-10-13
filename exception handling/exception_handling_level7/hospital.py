class InvalidPatientError(Exception):
    pass
class Hospital:
    def register_patient(self, name, age):
        try:
            if not name.strip() or age <= 0:
                raise InvalidPatientError("Invalid patient information")
            print("Patient registered:", name, age)
        except InvalidPatientError as e:
            print(e)
hospital = Hospital()
hospital.register_patient("", 0)