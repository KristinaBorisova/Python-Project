import csv
from Hospital_Spetialist import Doctor, Nurse
from Hospital_Visitor import Patient, Visitor
import Specialization_type


def display_dictionaty_conent(some_dictionary):
    for key, value in some_dictionary.items():
        print(key, ":", str(value))


def display_tuple_content(some_tuple):
    for index, item in enumerate(some_tuple):
        print(index, item)


# Iterate through list and display indexed content
def display_list_content(some_list):
    for index in range(len(some_list)):
        element = some_list[index]
        print(index + 1, element)


def update_Patients_data_csv(some_lists):
    # Define Header of file
    header = ["First-Name", "Last-Name", "Age", "Gender", "Phone", "Visitor Type" "has_Symptoms", "Is_Injured"]
    # Define file name
    filename = "./patients_data.csv"
    data = some_lists
    # Open CSV file for writing
    with open(filename, "w", newline="") as file:
        # Create a wrigint object - csv writer
        csvwriter = csv.writer(file)
        # Write the header to the file
        csvwriter.writerow(header)
        # Add the data to the file
        csvwriter.writerows(data)


def update_Visitors_data_csv(some_list):
    # Define Header of file
    header = ["First-Name", "Last-Name", "Age", "Gender", "Phone", "Visitor Type" "has_appointment"]
    # Define file name
    filename = "./visitors_data.csv"
    data = some_list
    # Open CSV file for writing
    with open(filename, "w", newline="") as file:
        # Create a wrigint object - csv writer
        csvwriter = csv.writer(file)
        # Write the header to the file
        csvwriter.writerow(header)
        # Add the data to the file
        csvwriter.writerows(data)


def update_Specialists_data_csv(some_list):
    # Define Header of file
    header = ["First-Name", "Last-Name", "Age", "Gender" "Type", "Specialization", "Experience"]
    # Define file name
    filename = "./specialists_data.csv"
    data = some_list
    # Open CSV file for writing
    with open(filename, "w", newline="") as file:
        # Create a wrigint object - csv writer
        csvwriter = csv.writer(file)
        # Write the header to the file
        csvwriter.writerow(header)
        # Add the data to the file
        csvwriter.writerows(data)


def add_new_specialist():
    print("Please enter person's full name:")
    fullName = input()
    firstName, *lastName = fullName.split()
    print("Please enter age:")
    age = int(input())
    gender = input("Please enter gender:")
    doctor_type = input(("Please enter Specialization type(Doctor/Nurse):"))
    if doctor_type == "Doctor":
        specialization = input("Please choose type of specialization:\n Surgery\n Neurology \n Orthopedics \n GP: ")
        experience = int(input("Years of experience:"))
        specialistObj = Doctor(firstName, *lastName, age, gender, doctor_type, specialization, experience)
    elif doctor_type == "Nurse":
        experience = int(input("Years of experience:"))
        specialistObj = Nurse(firstName, lastName, age, gender, doctor_type, experience)

    return specialistObj


def add_new_patient():
    print("Please enter person's full name:")
    fullName = input()
    firstName, *lastName = fullName.split()
    print("Please enter age:")
    age = int(input())
    gender = input("Please enter gender:")
    phoneNumb = input(("Please enter phone number in the format (+359)-xxx-xxx-xxx:"))
    visitor_type = Visitor_type.PATIENT
    has_symptoms = int(input("Does the patient have any symptoms?(True/False):"))
    patientObj = Patient(firstName, *lastName, age, gender, phoneNumb, has_symptoms)

    return patientObj


def add_new_visitor():
    print("Please enter person's full name:")
    fullName = input()
    firstName, *lastName = fullName.split()
    print("Please enter age:")
    age = int(input())
    gender = input("Please enter gender:")
    phoneNumb = input(("Please enter phone number in the format (+359)-xxx-xxx-xxx:"))
    visitor_type = Visitor_type.VISITOR
    has_symptoms = int(input("Does the visitor have an appointment?(True/False):"))
    visitorObj = Patient(firstName, *lastName, age, gender, phoneNumb, has_symptoms)

    return visitorObj


def show_avg_waiting_time():
    print("Please choose the type of visiotr (Patient | Visitor):")
    type_of_visitor = Visitor_Type.Patient | Visitor_Type.Visitor
    # numb_of_patients = len ( List of patients)
    # numb_of_visitors = len (list of visitors)
    # if(type_of_visitor = Visisotr_Type.Patient):
    # avg_Waiting_Time = numb_of_patients * 10
    # elif(type_of_visitor = Visisotr_Type.Visitor):
    # avg_Waiting_Time = numb_of_patients * 20
    # return avg_waiting_time
