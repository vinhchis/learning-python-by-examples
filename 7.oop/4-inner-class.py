class Outer: 
    def __init__(self): 
        self.outer_attr = "Outer attribute" 
        self.inner_instance = self.Inner()   # Creating an instance of Inner class 
 
    def outer_method(self): 
        print("This is an outer method") 
 
    class Inner: 
        def __init__(self): 
            self.inner_attr = "Inner attribute" 
 
        def inner_method(self): 
            print("This is an inner method") 
 
 
# Creating an instance of the Outer class 
outer_instance = Outer() 
 
# Accessing outer class attributes and methods 
print(outer_instance.outer_attr) 
outer_instance.outer_method() 

# Accessing inner class attributes and methods inner instance 
print(outer_instance.inner_instance.inner_attr)
outer_instance.inner_instance.inner_method() 