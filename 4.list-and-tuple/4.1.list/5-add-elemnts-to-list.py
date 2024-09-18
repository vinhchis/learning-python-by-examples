# 1. append()
a_list = [1, 2, 3]
a_list.append(4)
# Adds 4 to the end of the list
print(a_list)

# 2. insert() with index
i_list = [1, 2, 3]
i_list.insert(1, 5)
i_list.insert(5, 10)
i_list.insert(7, 20) # if index is greater than length of list (size) -> insert to list[size]
# Inserts 5 at index 1
print(i_list)
# Output: [1, 5, 2, 3]

# 3. concatenation() (+) method
c_list = [1, 2, 3]
new_elements = [4, 5]
c_list += new_elements
# Concatenates the two lists
print(c_list)
# Output: [1, 2, 3, 4, 5]