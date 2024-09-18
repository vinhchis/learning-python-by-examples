my_tuple = (1, 2, 3, 4, 5)
# Accessing individual elements by index
element_at_index_0 = my_tuple[0]
print("Element at index 0:", element_at_index_0)
 # Output: 1
element_at_index_2 = my_tuple[2]
print("Element at index 2:", element_at_index_2)
 # Output: 3
# Negative indexing (counting from the end)
last_element = my_tuple[-1]
print("Last element:", last_element) # Output: 5
second_last_element = my_tuple[-2]
print("Second last element:", second_last_element)
 # Output: 4
# Slicing to retrieve a segment of the tuple.
slice1 = my_tuple[1:4]
print("Slice 1:", slice1) # Output: (2, 3, 4)
slice2 = my_tuple[:3]
print("Slice 2:", slice2)
 # Output: (1, 2, 3)
slice3 = my_tuple[2:]
print("Slice 3:", slice3)
 # Output: (3, 4, 5)