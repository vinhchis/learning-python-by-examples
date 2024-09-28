# use abstract method same as decorator in python
from abc import ABC, abstractmethod 
 
class Shape(ABC): 
    @abstractmethod 
    def area(self): 
        pass 
 
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
 
    def area(self): 
        return 3.14 * self.radius * self.radius 
 
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
    def area(self): 
        return self.width * self.height 
 
# Creating instances of the subclasses 
# shape = Shape() # Can't instantiate abstract class Shape without an implementation for abstract method 'area' 
circle = Circle(5) 
rectangle = Rectangle(4, 6) 
 
# Calculating and printing the areas   
print("Area of Circle:", circle.area()) 
print("Area of Rectangle:", rectangle.area())