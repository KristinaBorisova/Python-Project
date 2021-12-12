from main import doctors_shifts, patients_list, visitors_list, specialists_list
from menu_Manager import *

"""
Main program's menu is started from here
"""


class menu:
    def display_menu():
        print("----User Menu----")
        print("[1] Show Specialists' Weekly Schedule")
        print("[2] Show list of Specialists")
        print("[3] Show list of Patients")
        print("[4] Show list of Visitors")
        print("[5] Register a new Specialist")
        print("[6] Register a new Patient")
        print("[7] Register a new Visitor")
        print("[8] Show average waiting time")
        print("[0] Exit Menu")
        print("----------------")

    display_menu()
    option = int(input("Please enter your option:"))

    while option != 0:
        if option == 1:
            print("\n<<You have chosen to see the hospital Specialists' Weekly Schedule>>")
            print("=====Doctors' Shifts DICTIONARY=====")
            display_dictionaty_conent(doctors_shifts)
            print("===================================\n")
        elif option == 2:
            print("<<You have chosen to view the list of Specialists>>")
            display_list_content(specialists_list)

        elif option == 3:
            print("<<You have chosen to view the list of Patients in the waiting room>>")
            display_list_content(patients_list)

        elif option == 4:
            print("\n<<You have chosen to view the list of Visitors>>")
            display_list_content(visitors_list)
        elif option == 5:
            print("\n<<You have chosen to add a new Specialist>>")
            add_new_specialist()

        elif option == 6:
            print("\n<<You have chosen to add a new Patient>>")
        elif option == 7:
            print("<<You have chosen to add a new Visitor>>")
        elif option == 8:
            print("<<You have chosen to see the Average Waiting Time>>")
        else:
            print("Invalid Optoin. Please try again!")

        print()
        display_menu()
        option = int(input("Enter your option:"))


print("Actions completed. Thank you for using this program!")
