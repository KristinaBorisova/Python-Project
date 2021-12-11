from enum import Enum

# User to make the filtering of doctors and nurses easier
class Specialist_Type(Enum):
    SURGEON = "s"
    NEUROLOGIST = "n"
    ORTHOPEDIC = "o"
    GP = "gp"
    NURSE = "n"
    