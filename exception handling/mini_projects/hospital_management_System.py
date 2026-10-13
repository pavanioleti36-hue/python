from datetime import datetime
class InvalidPatientError(Exception): pass
class DoctorUnavailableError(Exception): pass
class InvalidAppointmentDateError(Exception): pass
class Hospital:
    def __init__(self):
        self.doctors = ["Dr. Kumar", "Dr. Priya"]
    def book_appointment(self, patient, age, doctor, date):
        try:
            if not patient.strip() or age <= 0:
                raise InvalidPatientError("Invalid patient details")
            if doctor not in self.doctors:
                raise DoctorUnavailableError("Doctor unavailable")
            appointment_date = datetime.strptime(date, "%Y-%m-%d").date()
            if appointment_date < datetime.today().date():
                raise InvalidAppointmentDateError("Appointment date cannot be in the past")
            print("Appointment booked for", patient)
        except (InvalidPatientError, DoctorUnavailableError, InvalidAppointmentDateError, ValueError) as e:
            print("Error:", e)
hospital = Hospital()
hospital.book_appointment("Ravi", 20, "Dr. Kumar", "2027-01-15")