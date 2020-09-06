class User:
    """
    class that generates new instance of user details
    """
    user_list = []
    
    def _init_(self,first_name,last_name,number,email):
    
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email= email