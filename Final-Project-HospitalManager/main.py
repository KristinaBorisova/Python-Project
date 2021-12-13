from typing import ClassVar
from Hospital_Visitor import *
from Hospital_Spetialist import *
from Menu import *
from enum import Enum
from Specialization_type import *

doctors_shifts = {
    "Monday": Specialization_type.SURGEON.value,
    "Tuesday": Specialization_type.NEUROLOGIST.value,
    "Wednesday": Specialization_type.ORTHOPEDIC.value,
    "Thursday": Specialization_type.GP.value,
    "Friday": Specialization_type.SURGEON.value,
}

specialists_list = [["First Name", "Last Name", 50, "Doctor", "Specialization", 25]]

patients_list = [["Patient Name", "Patient LastName", 35, "Female", "+359-886-666-777", True]]

visitors_list = [
    ["Visitor1", "LastName1", 35, "male", "+359-886-666-777", Visitor_Type.VISITOR, False],
    ["Visitor2", "LastName2", 35, "male", "+359-886-666-777", Visitor_Type.VISITOR, False],
]


def update_doctors_list(some_Instance):
    if some_Instance not in specialists_list:
        specialists_list.append(str(some_Instance))


def add_visitor_to_list(some_Instance):
    if some_Instance not in visitors_list:
        visitors_list.append(str(some_Instance))


def main():

    # Visitor: First Name; Last Name; Age; Gender; Phone; Visitor Type, has Appointment)
    visitor2 = Visitor("VisitorName2", "LastName2", 42, "female", "(+359) 886 777 888", Visitor_Type.VISITOR, True)
    visitor3 = Visitor("Visitor3", "LastName3", 33, "male", "+359-886-666-777", Visitor_Type.VISITOR, False)
    visitors_list.append(str(visitor3))

    print("DOCTORS INFO")
    # Doctors: First Name; Last Name; Age; Gender; Doctor Type; Experience, specialization)
    nurse1 = Nurse("Maria", "Manova", 45, "female", Doctor_Type.Nurse, 15)
    doctor2 = Doctor("Ivan", "Ivanov", 55, "male", Doctor_Type.Doctor, 20, Specialization_type.GP)
    print(str(doctor2))
    print(str(nurse1))

    # check if doctor1 is in list
    update_doctors_list(str(doctor2))
    update_doctors_list(str(nurse1))

    print("Specialists' list::::::::")
    display_list_content(specialists_list)

    print("Visitors' list::::::::::")
    display_list_content(visitors_list)


if __name__ == "__main__":
    main()
