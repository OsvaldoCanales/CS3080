'''
Homework 4, Excercise 2
Osvaldo Canales
March 7, 2023
Develop a program with two methods that find phone numbers and email addresses 

'''

import re

#User can paste the text into the variable "text"
#Example text
text = '''Hello, my name is John Doe and my phone number is (555) 555-5555.
You can also reach me at john.doe@example.com. If I am not availabe for these options, my friend Tim can also be contacted
at (719)453-3234. Thanks!'''

#Method that finds only phone numbers 
def find_phone_numbers(text):
    # Regular expression to match phone numbers
    pattern = re.compile(r'\b\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\b')
    # Find all matches in the text
    matches = re.findall(pattern, text)
    # Print all matches to the screen
    for match in matches:
        print('Phone numbers found:', '-'.join(match))

#Method that finds only email addresses in a text 
def find_email_addresses(text):
    # Regular expression to match email addresses
    # Note that lower case and upper case letters are accounted 
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Find all matches in the text
    matches = re.findall(pattern, text)
    # Print all matches to the screen
    for match in matches:
        print('Email addresses found:', match)

# Call the functions with the given text
find_phone_numbers(text)
find_email_addresses(text)
