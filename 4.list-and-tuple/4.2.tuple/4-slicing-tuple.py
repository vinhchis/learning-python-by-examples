my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Accessing individual elements by index
element_at_index_0 = my_tuple[0]
print("Element at index 0:", element_at_index_0)
 # Output: 1

element_at_index_2 = my_tuple[2]
print("Element at index 2:", element_at_index_2)
 # Output: 3

# Negative indexing (counting from the end)
last_element = my_tuple[-1]
print("Last element:", last_element) 
# Output: 9
second_last_element = my_tuple[-2]
print("Second last element:", second_last_element)
 # Output: 8

# Slicing to extract a portion of the tuple
slice1 = my_tuple[1:4]
print("Slice 1:", slice1) # Output: (2, 3, 4)
slice2 = my_tuple[:3]
print("Slice 2:", slice2)
 # Output: (1, 2, 3)
slice3 = my_tuple[3:]
print("Slice 3:", slice3)
 # Output: (4, 5, 6, 7, 8, 9)

# Using negative indexing in slicing
slice4 = my_tuple[-5:-2]
print("Slice 4:", slice4) # Output: (5, 6, 7)
# Slicing with a step
slice5 = my_tuple[::2]
print("Slice 5:", slice5)
 # Output: (1, 3, 5, 7, 9)
slice6 = my_tuple[1::2]
print("Slice 6:", slice6)
 # Output: (2, 4, 6, 8)
 
# Reversing a tuple using slicing
reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)
 # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1)