class HospitalPatient:
    def __init__(self, name, age, patient_id, disease, doctor):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.disease = disease
        self.doctor = doctor

    def display_info(self):
        print("Patient Name:", self.name)
        print("Age:", self.age)
        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)
        print("Doctor Assigned:", self.doctor)
        print("-------------------------")

patient1 = HospitalPatient("Ravi Kumar", 45, "P001", "Diabetes", "Dr. Ramesh")
patient2 = HospitalPatient("Sita Devi", 32, "P002", "Asthma", "Dr. Priya")
patient3 = HospitalPatient("Arjun", 60, "P003", "Heart Disease", "Dr. Kiran")

patient1.display_info()
patient2.display_info()
patient3.display_info()
