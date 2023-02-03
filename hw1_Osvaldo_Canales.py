'''
Homework 1
Name: Osvaldo Canales
Date: January 31, 2023
Description of your program: We will develop questions for the user to answer.
'''


import random 

# declare constants 
MAX_QUESTIONS = 3
MAX_GUESSES = 3

print('Hello! In order to sign in I need you to answer some simple questions ')

for index in range(1):

    #First question will ask their name and state how many characters there are
    print('What is your name?')
    userName = input()
    numberOfLetters = str(len(userName))
    print('Hello! ' +userName ,'\nDid you know that your name is ' +numberOfLetters, 'long?')
    MAX_QUESTIONS +=1

    #Try to guess the user's age and generate a random number from 0 to 50.
    print('I bet I can guess your age!')
    print('I bet it is '+str(random.randint(0,50)),'which is probably wrong.') 
    print('How old are you?')
    userAge = int(input())
    print('You are ' +str(userAge),'years old? I think I was pretty close.')

    #Second question will ask them for a slow animal
    print('Think of the slowest animal in the world and enter it.')

    #Capitalize the input for user error 
    animalGuess = input()
    capitalGuess = animalGuess.capitalize();

    #Try to guess that the user entered one below and give a secret fun fact!
    slowAnimals = ['Snail','Sloth','Turtle']
  
    if capitalGuess == slowAnimals[0]:
            print('Fun fact about snails: ')
            print('Wild snails live from 3 to 7 years, while those in captivity can live up to 25 years.')

    elif capitalGuess == slowAnimals[1]:
            print('Fun fact about sloths: ')
            print("There are only 2 groups of sloths in the world.")

    elif capitalGuess == slowAnimals[2]:
            print('Fun fact about turtles: ')
            print('Did you know that turtles do not have teeth?')

    else:
            print(capitalGuess + 's are pretty slow. I just wanted to know. ')

    MAX_QUESTIONS +=1

    #Third question will have them guess what fast animal I am thinking of. 
    #This is what they are trying to guess. 
    fastAnimal = 'Cheetah'
    numGuesses = 1
    correctAnswer = False
    

    #Loop until they guess or they run out of guesses
    while numGuesses <= MAX_GUESSES:
        print('I am thinking of a very fast animal. Can you try to guess what animal that is? I will only give you two chances to guess.')
        userGuess = input()
        capitalCheetah = userGuess.capitalize()

        #if the user guesses the answer then break out of the loop
        if capitalCheetah == fastAnimal:
            print('Correct! That is what I was thinking!')
            correctAnswer = True
            if correctAnswer == True:
                break

        elif userGuess != fastAnimal and numGuesses == 1: 
            print('Wrong! Let me give you a hint:')
            print ('They are built for super speed, rather than stamina')
            numGuesses = numGuesses + 1

        elif userGuess != fastAnimal and numGuesses == 2: 
            print('Wrong! Let me give you another hint:')
            print('They have a recognizable characteristic of being "spotted"')
            numGuesses = numGuesses + 1

         # if the user runs out of guesses then break out of the loop with the statement 
        else:
            print('You ran out of guesses!')
            break

    #Max questions are met so exit out of for loop 
    MAX_QUESTIONS +=1
    if index == MAX_QUESTIONS: break
else: 
    print('Thanks for playing!')
        
            


    










