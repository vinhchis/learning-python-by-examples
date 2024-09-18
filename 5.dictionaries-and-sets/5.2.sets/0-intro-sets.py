# Creating a set
fruits = {"apple", "banana", "orange"}
# Adding elements to the set
fruits.add("grape")
# Removing an element from the set
fruits.remove("banana")
# Checking membership
print("Is 'apple' in the set?", "apple" in fruits)
# Iterating through the set
print("Fruits in the set:")
for fruit in fruits:
    print(fruit)