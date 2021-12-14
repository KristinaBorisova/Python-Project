from Person import Person
from enum import Enum

# Diferentiating between different types of visitors
class Visitor_Type(Enum):
    PATIENT = "Patient"
    VISITOR = "Visitor"


class Hospital_Visitor(Person):
    waiting_time = 10

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type):
        super().__init__(first_name, last_name, age, gender, phone)
        self.visitor_type = visitor_type


class Patient(Hospital_Visitor):
    waiting_time = 10
    # a class variable to hold a list of all Patients that have been created
    all_Patients = []

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type, has_symptoms):
        super().__init__(first_name, last_name, age, gender, phone, visitor_type)
        self.has_symptoms = has_symptoms
        self.visitor_type = Visitor_Type.PATIENT
        self.__class__.all_Patients.append(self)  # add the newly created instance to the list


class Visitor(Hospital_Visitor):
    waiting_time = 20
    # a class variable to hold a list of all Visitors that have been created
    all_Visitors = []

    def __init__(self, first_name, last_name, age, gender, phone, visitor_type, has_appointment):
        super().__init__(first_name, last_name, age, gender, phone, visitor_type)
        self.has_appointment = has_appointment
        self.visitor_type = Visitor_Type.VISITOR
        self.__class__.all_Visitors.append(self)  # add the newly created instance to the list
