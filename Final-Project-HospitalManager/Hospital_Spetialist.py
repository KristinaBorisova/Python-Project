from typing import Iterable
from Person import Person
from enum import Enum
import Specialization_type


class Doctor_Type(Enum):
    Doctor = "Doctor"
    Nurse = "Nurse"


class Hospital_Worker(Person):
    def __init__(self, first_name, last_name, age, gender, doctor_type, experience):
        super().__init__(first_name="noname", last_name="nolastName", age=0)
        self.doctor_type = doctor_type
        self.experience = experience


class Doctor(Hospital_Worker):
    # a class variable to hold a list of all Doctors that have been created
    all_Doctors = []

    def __init__(self, first_name, last_name, age, gender, doctor_type, experience, specialization_type):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.doctor_type = doctor_type
        self.experience = experience
        self.specialization_type = specialization_type
        self.__class__.all_Doctors.append(self)  # add the newly created instance to the list

    def __next__(self):
        return self

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def as_list(self):
        return [getattr(self, fieldname) for fieldname in self._fields_list]


class Nurse(Hospital_Worker):
    # a class variable to hold a list of all Nurses that have been created
    all_Nurses = []

    def __init__(self, first_name, last_name, age, gender, doctor_type, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.doctor_type = doctor_type
        self.experience = experience
        self.__class__.all_Nurses.append(self)  # add the newly created instance to the list

    def __next__(self):
        return self

    def __str__(self):
        return str(self.__class__) + "," + str(self.__dict__)
