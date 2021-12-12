from Person import Person
from enum import Enum
import Specialist_Type



class Hospital_Worker(Person):
    def __init__(self, first_name, last_name, age, specialization_type):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.specialization_type = specialization_type


class Doctor(Hospital_Worker):
    def __init__(self, first_name, last_name, age, specialization_type, experience):
        super().__init__(first_name="noname", last_name="nolastName", specialization_type="non", age=0)
        self.specialization_type = specialization_type
        self.experience = experience


class Nurse(Hospital_Worker):
    def __init__(self, first_name, last_name, age, TYPE, experience):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.TYPE = TYPE
        self.experience = experience
