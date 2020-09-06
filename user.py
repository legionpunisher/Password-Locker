class User:
    """
    class that generates new instance of user details
    """
    user_list = []
    
    def __init__(self,first_name,last_name,number,email):
    
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email= email
    
    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)