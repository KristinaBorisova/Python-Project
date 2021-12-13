from typing import ClassVar
from Hospital_Visitor import *
from Hospital_Spetialist import *
from menu import *
from enum import Enum
import inspect
from Specialization_type import *
import csv

doctors_shifts = {
    "Monday": Specialization_type.SURGEON.value,
    "Tuesday": Specialization_type.NEUROLOGIST.value,
    "Wednesday": Specialization_type.ORTHOPEDIC.value,
    "Thursday": Specialization_type.GP.value,
    "Friday": Specialization_type.SURGEON.value,
}

specialists_list = [["First Name", "Last Name", 50, "Doctor", "Surgeon", 25]]

patients_list = []

visitors_list = [
    ["Visitor1", "LastName1", 35, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False],
    ["Visitor2", "LastName2", 35, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False],
]


def main():
    # Visitor: First Name; Last Name; Age; Gender; Phone; Visitor Type, has Appointment)
    visitor2 = Visitor("Name2", "LastName2", 42, "female", "(+359) 886 777 888", VISITOR_TYPE.VISITOR, True)
    visitor3 = Visitor("Visitor3", "LastName3", 33, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False)
    visitors_list.append(visitor3)

    def add_visitor(visitor):
        if visitor not in visitors_list:
            visitors_list.append(visitor3)

    print(visitors_list, "\n")
    # managerMenu = menu



if __name__ == "__main__":
    main()
