'''
Homework 2, Excercise 4_1
Osvaldo Canales
February 14, 2023
Guess the number  
'''

import random

# generate a random number between 1 and 20
NUMBER = random.randint(1, 20)

# set the maximum number of tries
MAX_TRIES = 10

# start the game
print("I'm thinking of a number between 1 and 20. You have 10 tries.")

for try_num in range(1, MAX_TRIES + 1):
    # get the player's guess
    guess = input("Guess #" + str(try_num) + ": ")
    # convert the input to an integer
    guess = int(guess)  
    
    # check if the guess is correct
    if guess == NUMBER:
        print("Good Job! You guessed my number in " + str(try_num) + " guesses.")
        break  # end the game
    
    # provide a hint
    if guess < NUMBER:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
        
    # check if it's the last try
    if try_num == MAX_TRIES:
        print("Sorry, the number I was thinking of was " + str(NUMBER) + ".")
