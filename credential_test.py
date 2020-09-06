import unittest
from credentials import Credential

class TestUser (unittest.TestCase):
    """
    test class that defines test cases for the user class behaviour.
    """
    #First test
    def setUp(self):
        """
        setUp method to run before each test cases.
        """
        self.new_credential = Credential("legionpunisher","shadow521","Facebook")
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        
        self.assertEqual(self.new_credential.username,"Moses")
        self.assertEqual(self.new_credential.password,"shadow521")
        self.assertEqual(self.new_credential.account,"Facebook")
        