class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []
    def __init__(self,username,password):
        self.username = username
        self.password = password