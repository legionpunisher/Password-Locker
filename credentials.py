import pyperclip
class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []
    def __init__(self,username,password,account):
        self.username = username
        self.password = password
        self.account = account
        
    def save_credential(self):
        
        """
        save_credential method saves credential objects into credentail_list
        """
        
        Credential.credential_list.append(self)
        
    def  delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)
        
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a account and returns a credential that matches that account.

        Args:
            account: account to search for
        Returns :
            credential of person that matches the account.
        '''

        for credential in cls.credential_list:
            if credential.account == account:
                return credential
            
    @classmethod
    def credential_exist(cls,account):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account: account to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                    return True
                
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
    