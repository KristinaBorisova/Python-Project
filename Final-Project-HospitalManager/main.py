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

specialists_list = []

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


#   print(visitor1.get_last, "|", visitor2.get_last)

# patient1 = Patient("Name3", "LastName3", "50", VISITOR_TYPE.PATIENT, False, False)
# patient2 = Patient("Name4", "LastName4", "20", VISITOR_TYPE.PATIENT, False, True)


# doctor1 = Doctor("Name1", "LastName", "20", SPECIALIST_TYPE.DOCTOR, "cardiology", 15)
# doctor2 = Nurse("Name2", "LastName2", "30", SPECIALIST_TYPE.NURSE, 10)


if __name__ == "__main__":
    main()
