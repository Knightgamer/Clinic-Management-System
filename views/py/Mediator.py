class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def notify(self, sender, event):
        print(f"Mediator handling '{event}' from {sender}")

class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

class PatientManagementModule(Colleague):
    def update_patient_record(self):
        self.mediator.notify(self, "update_patient_record")

class AppointmentModule(Colleague):
    def schedule_appointment(self):
        self.mediator.notify(self, "schedule_appointment")

# Client code
mediator = ConcreteMediator()
patient_management = PatientManagementModule(mediator)
appointment_module = AppointmentModule(mediator)

patient_management.update_patient_record()
appointment_module.schedule_appointment()
