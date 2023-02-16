'''
Homework 2, Excercise 4_3
Osvaldo Canales
February 14, 2023
Guess the number but with bounds and an automatic guesser 
'''

import random

# generate random lower and upper bounds between 1 and 100
LOWER = random.randint(1, 50)
UPPER = random.randint(51, 100)

# set the maximum number of tries
MAX_TRIES = 10

# start the game
print("I'm thinking of a number between " + str(LOWER) + " and " + str(UPPER) + ". You have 10 tries.")

# generate the random number within the bounds
NUMBER = random.randint(LOWER, UPPER)

# initialize a list to keep track of the automatic player's guesses
previous_guesses = []

for try_num in range(1, MAX_TRIES + 1):
    # generate a new guess that is not in the list of previous guesses
    guess = random.randint(LOWER, UPPER)
    while guess in previous_guesses:
        guess = random.randint(LOWER, UPPER)
    
    # add the guess to the list of previous guesses
    previous_guesses.append(guess)
    
    # check if the guess is correct
    if guess == NUMBER:
        print("The automatic player guessed the number " + str(NUMBER) + " in " + str(try_num) + " tries.")
        break  # end the game
    
    # provide a hint
    if guess < NUMBER:
        print("The automatic player guessed " + str(guess) + ". It's too low.")
    else:
        print("The automatic player guessed " + str(guess) + ". It's too high.")
        
    # check if it's the last try
    if try_num == MAX_TRIES:
        print("Sorry, the number I was thinking of was " + str(NUMBER) + ".")

