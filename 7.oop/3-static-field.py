class Dog: 
    species = "Canine"  # This is a class attribute 
 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
 
# Create instances of the Dog class 
dog1 = Dog("Buddy", 3) 
dog2 = Dog("Molly", 5)

# Access class attribute using the class name 
print(f"{dog1.name} is a {Dog.species}") 
print(f"{dog2.name} is a {Dog.species}") 

Dog.species = "Canis familiaris"  # Modify the class attribute 
 
print(f"{dog1.name} is a {Dog.species}") 
print(f"{dog2.name} is a {Dog.species}") 