class hospital:
    def __init__(self, pateint_name, age, disease, doctor_name):
        self.pateint_name = pateint_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name
    def display(self):
        print("Pateint Name:", self.pateint_name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor Name:", self.doctor_name)
hospital1 = hospital("kailash", 25, "fever", "dr.sai")
hospital2 = hospital("sukumar", 30, "cold", "dr.rupa")
hospital3 = hospital("kalyani", 28, "headache", "dr.pavani")            
hospital1.display()
hospital2.display()
hospital3.display()