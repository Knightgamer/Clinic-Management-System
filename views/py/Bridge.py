# Implementor
class UserActions:
    def execute_action(self):
        pass

# Concrete Implementors
class ManagePatients(UserActions):
    def execute_action(self):
        print("Managing patients...")

class ManageRecords(UserActions):
    def execute_action(self):
        print("Managing records...")

# Abstraction
class UserRole:
    def __init__(self, actions: UserActions):
        self.actions = actions

    def perform_action(self):
        pass

# Refined Abstraction
class DoctorRole(UserRole):
    def perform_action(self):
        print("Doctor Role:")
        self.actions.execute_action()

class ReceptionistRole(UserRole):
    def perform_action(self):
        print("Receptionist Role:")
        self.actions.execute_action()

# Client code
# Doctors and Receptionists can manage both patients and records, showing the flexibility of the Bridge pattern.
doctor_manages_patients = DoctorRole(ManagePatients())
doctor_manages_patients.perform_action()

receptionist_manages_records = ReceptionistRole(ManageRecords())
receptionist_manages_records.perform_action()
