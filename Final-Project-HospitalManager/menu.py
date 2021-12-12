from main import doctors_shifts, patients_list, visitors_list
from menu_Manager import *

"""
Main program's menu is started from here
"""


class menu:
    def display_menu():

        print("----User Menu----")
        print("[1] Show list of Doctors")
        print("[2] Show list of Patients")
        print("[3] Show list of Visitors")
        print("[4] Register a new Patient")
        print("[5] Register a new Specialist")
        print("[0] Exit Menu")
        print("----------------")

    display_menu()
    option = int(input("Please enter your option:"))

    while option != 0:
        if option == 1:
            print("<<You have chosen to view the list of Specialists Available>>")
            print("=====Doctors' Shift DICTIONARY=====")
            display_dictionaty_conent(doctors_shifts)

        elif option == 2:
            print("<<You have chosen to view the list of Patients in the waiting room>>")
            display_list_content(patients_list)

        elif option == 3:
            print("<<You have chosen to view the list of Visitors>>")
            display_list_content(visitors_list)
        elif option == 4:
            print("<<You have chosen to see the average waiting time>>")

        elif option == 5:
            print("<<You have chosen to add a new specialist/patient/visitor to the list>>")

        else:
            print("Invalid Optoin. Please try again!")

        print()
        display_menu()
        option = int(input("Enter your option:"))

    print("Actions completed. Thank you for using this program!")
