'''
Homework 4, Excercise 1
Osvaldo Canales
March 5, 2023
Write three classes with methods and calculate using them. 

'''

import math

#Parent class that 3 properties: area, parameter, and Diameter/Diagonal
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def diagonal_or_diameter(self):
        pass

#Child class with the shape "Rectangle"
class Rectangle(Shape):
    #Constructs the object when called 
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    #Caclulates the area
    def area(self):
        return self.length * self.width
    
    #Calculates the parimeter
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    #Calculates the diagonal
    def diagonal_or_diameter(self):
        return math.sqrt(self.length**2 + self.width**2)

#Child class for object "Circle"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    #Calculates the area
    def area(self):
        return math.pi * self.radius**2
    
    #Calculates the parimeter
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    #Calculates the diameter of the circle 
    def diagonal_or_diameter(self):
        return 2 * self.radius

    #Child class of Rectangle for object "Square"
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    #Calculate the diagonal
    def diagonal_or_diameter(self):
        return math.sqrt(2) * self.length

#Create a rectangle with a length of 20 and width of 10
rect = Rectangle(20, 10)

#Calculate a radius with the diagonal of the rectangle above
radius = 0.5 * rect.diagonal_or_diameter()

#Initialize a circle with the radius
circ = Circle(radius)
#Initialize a perimeter of the circle
perimeter = circ.perimeter()
#Display the output
print(perimeter)
