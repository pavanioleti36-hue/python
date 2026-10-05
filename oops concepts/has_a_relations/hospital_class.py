class Doctor:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Doctor:", self.name)


class Patient:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Patient:", self.name)


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Priya")
        ]

        self.patients = [
            Patient("Pavani"),
            Patient("Rahul")
        ]

    def show_details(self):
        print("Doctors:")
        for doctor in self.doctors:
            doctor.display()

        print("\nPatients:")
        for patient in self.patients:
            patient.display()


hospital = Hospital()
hospital.show_details()