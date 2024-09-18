class Person: 
    def __init__(self, name, age): 
# Prefixing with underscore indicates a "protected" attribute 
        self._name = name   
        self._age = age 
 
    # Getter methods 
    def get_name(self): 
        return self._name 
 
    def get_age(self): 
        return self._age 
 
    # Setter methods 
    def set_name(self, new_name): 
        if isinstance(new_name, str): 
            self._name = new_name 
        else: 
            print("Invalid name format.") 
 
    def set_age(self, new_age): 
        if isinstance(new_age, int) and new_age >= 0: 
            self._age = new_age 
        else: 
            print("Invalid age format.") 
 
    def display_info(self): 
        print(f"Name: {self._name}") 
        print(f"Age: {self._age}") 
 
 
# Create an instance of the Person class 
person = Person("Alice", 25) 
 
# Using getter methods 
print(f"Name: {person.get_name()}") 
print(f"Age: {person.get_age()}") 
 
# Using setter methods 
person.set_name("Alicia") 
person.set_age(26) 
# Display information using display_info method 
person.display_info() 