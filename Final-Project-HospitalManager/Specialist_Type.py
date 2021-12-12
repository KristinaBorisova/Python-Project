from enum import Enum

# User to make the filtering of doctors and nurses easier
class Specialist_Type(Enum):
    SURGEON = "Surgeon"
    NEUROLOGIST = "Neurologist"
    ORTHOPEDIC = "Orthopedic"
    GP = "General Practitioner"
    NURSE = "Nurse"
