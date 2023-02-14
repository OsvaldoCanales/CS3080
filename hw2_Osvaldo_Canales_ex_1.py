'''
Homework 2, Excercise 1 
Osvaldo Canales
February 14, 2023
Collatz Sequence program 
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
    userNumber = collatz(int(userNumber))
    