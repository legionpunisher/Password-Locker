class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []
    def __init__(self,username,password,account):
        self.username = username
        self.password = password
        self.account = account