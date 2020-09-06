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

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credentials()
    
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