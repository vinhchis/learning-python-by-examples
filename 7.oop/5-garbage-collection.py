import gc 
 
class Person: 
    def __init__(self, name): 
        self.name = name 
        print(f"Created instance for {self.name}") 
 
    def __del__(self): 
        print(f"Deleted instance for {self.name}") 
 
# Create instances of the Person class 
person1 = Person("Alice") 
person2 = Person("Bob") 
 
# Manually break reference to person2 
person2 = None 
 
# Force garbage collection 
print("Collecting garbage...") 
gc.collect() 
 
# The program might have a slight pause here as garbage collection is performed 
print("Garbage collection done.") 