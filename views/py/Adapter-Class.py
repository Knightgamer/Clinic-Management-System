class PatientManagementSystem:
    def add_patient(self, patient_info):
        pass

class NewPatientDataHandler:
    def create_patient_record(self, patient_info):
        print(f"Creating patient record: {patient_info}")

class PatientDataHandlerAdapter(PatientManagementSystem):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def add_patient(self, patient_info):
        self.adaptee.create_patient_record(patient_info)

# Client code
adaptee = NewPatientDataHandler()
adapter = PatientDataHandlerAdapter(adaptee)
adapter.add_patient({"name": "John Doe", "age": 30})
