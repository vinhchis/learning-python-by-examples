original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Extract elements from index 2 to index 5 (not including 5)
slice1 = original_list[2:5]
print("Slice 1:", slice1)

# Extract elements from index 3 to the end
slice2 = original_list[3:]
print("Slice 2:", slice2)

# Extract elements from the beginning to index 4 (not including 4)
slice3 = original_list[:4]
print("Slice 3:", slice3)

# Extract every alternate element, beginning from index 1.
slice4 = original_list[1::2]
print("Slice 4:", slice4)

# Reverse the list using a step of -1
reverse_list = original_list[::-1] # [ 0:end: -1]
print("Reversed List:", reverse_list)



# list[start:stop:step]