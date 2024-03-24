class MedicalRecord:
    def __init__(self):
        self.fields = {}

    def set_field(self, key, value):
        self.fields[key] = value

    def __str__(self):
        return str(self.fields)

class MedicalRecordBuilder:
    def __init__(self):
        self.medical_record = MedicalRecord()

    def add_title(self, title):
        self.medical_record.set_field("title", title)
        return self

    def add_date(self, date):
        self.medical_record.set_field("date", date)
        return self

    def build(self):
        return self.medical_record

# Client code
builder = MedicalRecordBuilder()
medical_record = builder.add_title("General Checkup").add_date("2024-03-24").build()
print(medical_record)
