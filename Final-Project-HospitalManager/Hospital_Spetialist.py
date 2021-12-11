from Person import Person
from enum import Enum



class Hospital_Worker(Person):
    def __init__(self, first_name, last_name, age, TYPE):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.TYPE = TYPE


class Doctor(Hospital_Worker):
    def __init__(self, first_name, last_name, age, TYPE, specialization, experience):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.TYPE = TYPE
        self.specialization = specialization
        self.experience = experience


class Nurse(Hospital_Worker):
    def __init__(self, first_name, last_name, age, TYPE, experience):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.TYPE = TYPE
        self.experience = experience
