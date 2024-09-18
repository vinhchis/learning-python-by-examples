class Rectangle: 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
 
    def calculate_area(self): 
        return self.width * self.height 
 
    @classmethod 
    def create_square(cls, side): 
        return cls(side, side) 
 
    @staticmethod 
    def is_large_rectangle(rect): 
        return rect.width * rect.height > 50 
 
 
# Creating instances of the Rectangle class 
rectangle1 = Rectangle(5, 10) 
rectangle2 = Rectangle.create_square(7) 
 
# Using instance methods 
area1 = rectangle1.calculate_area() 
area2 = rectangle2.calculate_area() 
 
# Using static method 
is_large1 = Rectangle.is_large_rectangle(rectangle1) 
is_large2 = Rectangle.is_large_rectangle(rectangle2) 
 
print(f"Area of rectangle1: {area1}") 
print(f"Area of rectangle2: {area2}") 

print(f"Is rectangle1 large? {is_large1}") 
print(f"Is rectangle2 large? {is_large2}") 