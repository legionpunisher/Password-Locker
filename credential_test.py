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
        
    #Third Test
    def tearDown (self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_multiple_credential (self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user","duolingo") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
        
    #Fourth Test
    def test_delete_credential (self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user","Github")
        test_credential.save_credential()  
                       
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)   
        
    #Fifth Test   
    def test_find_credential_by_account(self):
         
        '''
        test to check if we can find a credential by account and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","falcon456","duolingo") 
        test_credential.save_credential()

        found_credential = Credential.find_by_account("duolingo")
        self.assertEqual(found_credential.username,test_credential.username) 
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("legionpunisher","Test","duolingo") 
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("duolingo")

        self.assertTrue(credential_exists)
        
    def test_display_all_credentials (self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

        return False
    
if __name__ == '__main__':
    unittest.main()      