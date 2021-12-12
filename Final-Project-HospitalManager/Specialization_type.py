from enum import Enum

# User to make the filtering of doctors and nurses easier
class Specialization_type(Enum):
    SURGEON = "Surgeon"
    NEUROLOGIST = "Neurologist"
    ORTHOPEDIC = "Orthopedic"
    GP = "General Practitioner"
