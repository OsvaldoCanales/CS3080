'''
Homework 3, Excercise 2
Osvaldo Canales
February 21, 2023
Develop a program that counts the number of occurences of a letter of a string

'''

import pprint

#function will take in a string and count each character
def count_char(string):

    # Create an empty dictionary to store the character counts
    char_counts = {}

    # Loop through each character in the string
    for char in string:

        # Check if the character is already in the dictionary
        if char in char_counts:

            # If it is, increment its count by 1
            char_counts[char] += 1

        else:
            # If it isn't, add it to the dictionary with a count of 1
            char_counts[char] = 1

    return char_counts

#Create a string 
wordString = 'The quick brown fox jumps over the lazy dog'

#Print the number of occurences in each character
char_counts = count_char(wordString)
pprint.pprint(char_counts)