class UserFactory:
    def create_user(self):
        pass

    def create_session(self):
        pass

class DoctorFactory(UserFactory):
    def create_user(self):
        return Doctor()

    def create_session(self):
        return DoctorSession()

class ReceptionistFactory(UserFactory):
    def create_user(self):
        return Receptionist()

    def create_session(self):
        return ReceptionistSession()

class User:
    pass

class Session:
    pass

class Doctor(User):
    pass

class DoctorSession(Session):
    pass

class Receptionist(User):
    pass

class ReceptionistSession(Session):
    pass

# Client code
factory = DoctorFactory()
user = factory.create_user()
session = factory.create_session()
