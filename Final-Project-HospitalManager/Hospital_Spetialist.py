from Person import Person
from enum import Enum
import Specialization_type


class Doctor_Type(Enum):
    Doctor = "Doctor"
    Nurse = "Nurse"


class Hospital_Worker(Person):
    def __init__(self, first_name, last_name, age, doctor_type, experience):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.doctor_type = doctor_type
        self.experience = experience


class Doctor(Hospital_Worker):
    def __init__(self, first_name, last_name, age, doctor_type, specialization_type, experience):
        super().__init__(first_name, last_name, age, doctor_type, experience)
        self.specialization_type = specialization_type


class Nurse(Hospital_Worker):
    def __init__(self, first_name, last_name, age, doctor_type, experience):
        super().__init__(first_name, last_name, age, doctor_type, experience)
