from typing import ClassVar
from Hospital_Visitor import *
from Hospital_Spetialist import *
from Specialist_Type import *
from menu import *
from enum import Enum
import information

import csv

doctors_shifts = {
    "Monday": Specialist_Type.SURGEON.value,
    "Tuesday": Specialist_Type.NEUROLOGIST.value,
    "Wednesday": Specialist_Type.ORTHOPEDIC.value,
    "Thursday": Specialist_Type.GP.value,
    "Friday": Specialist_Type.NURSE.value,
}

patients_list = []

visitors_list = [
    ["Visitor1", "LastName1", 35, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False],
    ["Visitor1", "LastName1", 35, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False],
]


def main():

    visitor3 = Visitor("Visitor3", "LastName3", 33, "male", "+359-886-666-777", VISITOR_TYPE.VISITOR, False)
    visitor2 = Visitor("Name2", "LastName2", 42, "female", "(+359) 886 777 888", VISITOR_TYPE.VISITOR, True)
    visitors_list.append(visitor3)

    # managerMenu = menu

    # 1.create a new csv file and write in it
    """header = ["First-Name", "Last-Name", "Age", "Gender", "Priority", "WaitingTime"]
    data = [
        ["Alex", "Alexov", 35, "Male", "2", 10],
        ["Alex", "Alexov", 35, "Male", "2", 10],
        ["Alex", "Alexov", 35, "Male", "2", 10],
    ]
    filename = "./patients_data.csv"
    with open(filename, "w", newline="") as file:
        csvwriter = csv.writer(file)  # 2. create a csvwriter object
        csvwriter.writerow(header)  # 4. write the header
        csvwriter.writerows(data)  # 5. write the rest of the data"""
    # Visitor: First Name; Last Name; Age; Gender; Phone; Visitor Type, has Appointment)


#   print(visitor1.get_last, "|", visitor2.get_last)

# patient1 = Patient("Name3", "LastName3", "50", VISITOR_TYPE.PATIENT, False, False)
# patient2 = Patient("Name4", "LastName4", "20", VISITOR_TYPE.PATIENT, False, True)


# doctor1 = Doctor("Name1", "LastName", "20", SPECIALIST_TYPE.DOCTOR, "cardiology", 15)
# doctor2 = Nurse("Name2", "LastName2", "30", SPECIALIST_TYPE.NURSE, 10)


if __name__ == "__main__":
    main()
