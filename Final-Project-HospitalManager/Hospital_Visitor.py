from Person import Person
from enum import Enum

# Diferentiating between different types of visitors
class VISITOR_TYPE(Enum):
    PATIENT = "Patient"
    VISITOR = "Visitor"


class Hospital_Visitor(Person):
    waiting_time = 10

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type):
        super().__init__(first_name, last_name, age, gender, phone)
        self.visitor_type = visitor_type

class Patient(Hospital_Visitor):
    waiting_time = 5

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type, has_symptoms):
        super().__init__(first_name, last_name, age, gender, phone, visitor_type)
        self.has_symptoms = has_symptoms


class Visitor(Hospital_Visitor):
    waiting_time = 20

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type, has_appointment):
        super().__init__(first_name, last_name, age, gender,phone, visitor_type)
        self.has_appointment = has_appointment
        self.visitor_type = VISITOR_TYPE.VISITOR
