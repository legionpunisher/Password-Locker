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
        
        self.assertEqual(self.new_credential.username,"legionpunisher")
        self.assertEqual(self.new_credential.password,"shadow521")
        self.assertEqual(self.new_credential.account,"Facebook")
        
    #Second Test
    
    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)  
 
if __name__ == '__main__':
    unittest.main()      