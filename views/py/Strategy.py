class ViewStrategy:
    def view_patient_data(self, patient_id):
        pass

class DoctorViewStrategy(ViewStrategy):
    def view_patient_data(self, patient_id):
        print(f"Doctor viewing comprehensive data for patient {patient_id}")

class ReceptionistViewStrategy(ViewStrategy):
    def view_patient_data(self, patient_id):
        print(f"Receptionist viewing basic data for patient {patient_id}")

class PatientDataViewer:
    def __init__(self, strategy):
        self.strategy = strategy

    def display_patient_data(self, patient_id):
        self.strategy.view_patient_data(patient_id)

# Client code
strategy = DoctorViewStrategy()
viewer = PatientDataViewer(strategy)
viewer.display_patient_data(123)
