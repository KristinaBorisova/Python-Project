from typing import ClassVar
from Hospital_Visitor import *
from Hospital_Spetialist import *

# from menu import displayMenu
from enum import Enum

# import information
# import csv


def display_list_content(list):
    for index in range(len(list)):
        element = list[index]
        print(index + 1, element)


def main():

    hospital_specialists = [
        {"First name": "Name1", "Last_Name": 5, "age": 20},
        {"First name": "Name2", "Last_Name": 1, "age": 10},
        {"First name": "Name3", "Last_Name": 10, "age": 5},
    ]

    hospital_specialist2 = [
        {"Fist Name", "Last Name", 45, "Male", "Heart", "15"},
        {"Fist Name2", "Last Name2", 452, "Male2", "Heart2", "152"},
    ]
    # create a list for hospital patients
    hospital_patients = []

    # create a list for visitors
    hospital_visitors = []
    display_list_content(hospital_specialists)

    print("New List coming:::::")

    # Iterate through list and display indexed results
    display_list_content(hospital_specialist2)

    # visitor1 = Visitor("Name1", "LastName1", "20", VISITOR_TYPE.VISITOR, False)
    # visitor2 = Visitor("Name2", "LastName2", "30", VISITOR_TYPE.VISITOR, True)
    #   print(visitor1.get_last, "|", visitor2.get_last)

    patient1 = Patient("Name3", "LastName3", "50", VISITOR_TYPE.PATIENT, False, False)
    patient2 = Patient("Name4", "LastName4", "20", VISITOR_TYPE.PATIENT, False, True)

    doctor1 = Doctor("Name1", "LastName", "20", SPECIALIST_TYPE.DOCTOR, "cardiology", 15)
    doctor2 = Nurse("Name2", "LastName2", "30", SPECIALIST_TYPE.NURSE, 10)

    # hospital_specialists.append(visitor1)


if __name__ == "__main__":
    main()
