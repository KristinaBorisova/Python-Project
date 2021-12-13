from enum import Enum

# User to make the filtering of doctors and nurses easier
class Specialization_type(Enum):
    SURGEON = "Surgeon || Surgery"
    NEUROLOGIST = "Neurologist || Neurology"
    ORTHOPEDIC = "Orthopedist || Ortopetics"
    GP = "General Practitioner || General"
