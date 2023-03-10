'''
Homework 4, Excercise 2
Osvaldo Canales
March 7, 2023
Develop a program with a strong password check

'''
MAX_LENGTH = 8
import re

#Method where a password is tested 
def is_password_strong(password):
    # check if password is at least 8 characters long
    if len(password) < MAX_LENGTH:
        return False
    
    # check if password contains both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False
    
    # check if password has at least one digit
    if not re.search(r'\d', password):
        return False
    
    # password passed all checks
    return True


#while loop until user enters a strong password 
while True:
    #Ask the user to enter a password 
    print('Enter a password that has at least 8 characters long, contains both uppercase and lowercase letters, and at least one digit.')
    userPassword = input()

    if is_password_strong(userPassword):
        print('Password is strong')
        break
    else:
        print('Password is not strong, please enter a valid password.')

