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
    contact.delete_user()