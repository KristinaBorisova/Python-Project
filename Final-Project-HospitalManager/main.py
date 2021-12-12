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

patients_list = [["Fist_Name", "Second_Name", "Last_Name", 23, True, True]]
visitors_list = []


def main():

    # managerMenu = menu

    patient = Hospital_Visitor("Kristina", "Borisova", 23, "female", "patient")

    # 1.create a new csv file and write in it
    header = ["First-Name", "Last-Name", "Age", "Gender", "Priority", "WaitingTime"]
    data = [
        ["Alex", "Alexov", 35, "Male", "2", 10],
        ["Alex", "Alexov", 35, "Male", "2", 10],
        ["Alex", "Alexov", 35, "Male", "2", 10],
    ]
    filename = "./patients_data.csv"
    with open(filename, "w", newline="") as file:
        csvwriter = csv.writer(file)  # 2. create a csvwriter object
        csvwriter.writerow(header)  # 4. write the header
        csvwriter.writerows(data)  # 5. write the rest of the data

    hospital_specialists = [
        {"First name": "Name1", "Last_Name": 5, "age": 20},
        {"First name": "Name2", "Last_Name": 1, "age": 10},
        {"First name": "Name3", "Last_Name": 10, "age": 5},
    ]

    hospital_specialist2 = [
        {"Fist Name", "Last Name", 45, "Male", "Heart", "15"},
        {"Fist Name2", "Last Name2", 452, "Male2", "Heart2", "152"},
    ]

    display_list_content(hospital_specialists)

    print("New List coming:::::")

    # Create a tuple with Doctors' names
    # a_tuple = (1, 2, 3, 4)
    # display_tuple_content(a_tuple)


# visitor1 = Visitor("Name1", "LastName1", "20", VISITOR_TYPE.VISITOR, False)
# visitor2 = Visitor("Name2", "LastName2", "30", VISITOR_TYPE.VISITOR, True)
#   print(visitor1.get_last, "|", visitor2.get_last)

# patient1 = Patient("Name3", "LastName3", "50", VISITOR_TYPE.PATIENT, False, False)
# patient2 = Patient("Name4", "LastName4", "20", VISITOR_TYPE.PATIENT, False, True)


# doctor1 = Doctor("Name1", "LastName", "20", SPECIALIST_TYPE.DOCTOR, "cardiology", 15)
# doctor2 = Nurse("Name2", "LastName2", "30", SPECIALIST_TYPE.NURSE, 10)

# hospital_specialists.append(visitor1)


if __name__ == "__main__":
    main()
