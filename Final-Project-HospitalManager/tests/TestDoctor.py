import unittest
from Hospital_Spetialist import Doctor


class TestVisitor(unittest.testClass):
    def setUp(self):
       #setting instance attributes
        self.obj = Doctor("firstName", "lastName", 40, "d", "Cardiologist", 15)

    # Unittest for first name
    def test_correct_first_name(self):
        firstNameCheck = "firstName"
        self.assertEqual(firstNameCheck, self.obj.get_first)

    # Unittest for last name
    def test_correct_last_name(self):
        lastName = "lastName"
        self.assertEqual(lastName, self.obj.get_last)

    # Unittest for last name
    def test_correct_age(self):
        ageTest = 40
        self.assertEqual(ageTest, self.obj.get_age)
