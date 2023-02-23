'''
Homework 3, Excercise 1
Osvaldo Canales
February 23, 2023
Print the image of a 2D list using a nested for loop 

'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Nested for loop that will print the list above starting at the y index
for y in range(0,6):
    for x in range(0,9):
        if x == 8:
            print(grid[x][y])
            break
        print(grid[x][y], end = '')
