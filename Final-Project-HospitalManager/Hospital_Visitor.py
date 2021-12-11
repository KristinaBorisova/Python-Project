from Person import Person
from enum import Enum

# Diferentiating between different types of visitors
class VISITOR_TYPE(Enum):
    PATIENT = "p"
    VISITOR = "v"


class Hospital_Visitor(Person):
    def __init__(self, first_name, last_name, age, gender, TYPE):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.TYPE = TYPE

    def get_age(self):
        return super().get_age()

    def get_first(self):
        return super().get_first()

    def get_last(self):
        return super().get_last()


class Patient(Hospital_Visitor):
    def __init__(self, first_name, last_name, age, TYPE, has_symptoms, is_injured):
        super().__init__(first_name="noname", last_name="nolastName", age=0, TYPE="p")
        self.has_symptoms = has_symptoms
        self.is_injured = is_injured


class Visitor(Hospital_Visitor):
    def __init__(self, first_name, last_name, age, TYPE, has_appointment):
        super().__init__(first_name="noname", last_name="nolastName", age=0, TYPE="v")
        self.has_appointment = has_appointment
