import unittest
from user import User

class TestUser (unittest.TestCase):
    """
    test class that defines test cases for the user class behaviour.
    """
    #First test
    def setUp(self):
        """
        setUp method to run before each test cases.
        """
        self.new_user = User("Moses","Mbugua","0790437510","mbuguamoses656@gmail.com")
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        
        self.assertEqual(self.new_user.first_name,"Moses")
        self.assertEqual(self.new_user.last_name,"Mbugua")
        self.assertEqual(self.new_user.phone_number,"0790437510")
        self.assertEqual(self.new_user.email,"mbuguamoses656@gmail.com")
        
if __name__ == '__main__':
    unittest.main()
        