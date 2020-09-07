#!/usr/bin/env python3.8
from user import User
from credentials import Credential
def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def create_credential(username,password,account):
    '''
    Function to create a new credential
    '''
    new_credential= Credential(username,password,account)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
    
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
    
def find_credential(account):
    '''
    Function that finds a credential by account and returns the credential
    '''
    return Credential.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that account and return a Boolean
    '''
    return Credential.credential_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def main():
    print("Create a password_locker list. What is your name?")
    user_name = input()            
        
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
        
    while True:
                print('''Use these short codes :
                      cu - create a new user,
                      fu -find a user, 
                      eu -exit the user list,
                      cc -creare a new credential, 
                      dc -display credentials,                     
                      fc -find credentials                      
                      ec-exit the credential list''')
                
                                
                short_code = input().lower()

                if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')                 
                           
                elif short_code == 'fu':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_user(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("The above User does not exist")

                elif short_code == "ex":
                                     print("Have a lovely Day!")
                            
                elif short_code == "cc":
                                    print("New Credential")
                                    print("-"*5)
                    
                                    print("username....")
                                    username = input()
                    
                                    print("password...")
                                    password = input()
                    
                                    print("account...")
                                    account = input()
                                    
                                    save_credential(create_credential(username,password,account))# create a new credential.
                                    print ('\n')
                                    print(f"New Credential {username} {account} {password}created")
                                    print ('\n') 
                                                                                                           
                elif short_code == 'dc':

                            if display_credentials():
                                    print("A list of all you credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.username} {credential.password} .....{credential.account}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials under that account")
                                    print('\n')

                elif short_code == 'fc':

                            print("Enter an account e.g Facebook,duolingo")

                            search_account = input()
                            if check_existing_credentials(search_account):
                                    search_credential = find_credential(search_account)
                                    print(f"{search_credential.username} {search_credential.password}")
                                    print('-' * 20)

                                    print(f"username.......{search_credential.username}")
                                    print(f"password.......{search_credential.password}")
                            else:
                                    print("That credential does not exist")              
              
                elif short_code == "ec":
                                     print("Thank you have a lovely day!")                               

                break
    else:
                                    print("Invalid Input. Please use the short codes")


if __name__ == '__main__':

    main()
                               

