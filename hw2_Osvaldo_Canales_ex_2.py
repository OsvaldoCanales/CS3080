'''
Homework 2, Excercise 2
Osvaldo Canales
February 14, 2023
Collatz Sequence program with try and except
'''

#declare constant
COLLATZ_NUMBER = 1

#Function that tells if a number is even or odd and manipulates it 
def collatz(number):
    if (number % 2 ) == 0:
        print(number // 2 )
        return number // 2

    elif number % 2 == 1: 
        result = 3 * number + 1
        print (result)
        return result


#Ask the user to enter a digit 
userNumber = input('Hello! Please enter a digit: ')



#Loop until the number reaches the COLLATZ_NUMBER
while userNumber != COLLATZ_NUMBER:

    #The code will try the collatz sequence 
    try: 
        userNumber = collatz(int(userNumber))

    #if user did not enter a whole number then the program will break 
    except:
        print('Please use whole numbers only.')
        break