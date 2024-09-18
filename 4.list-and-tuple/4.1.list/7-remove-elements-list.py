# 1. remove()
r_list = [10, 20, 30, 40, 50, 30]
r_list.remove(30)
# Removes the value 30 from the list
print(r_list)
# [10, 20, 40, 50, 30]
print('----------------------------')

# 2. pop() method
p_list = [10, 20, 30, 40, 50]
removed_value = p_list.pop(2)
# Removes the element at index 2 (30)
print(removed_value)
# Output: 30
print(p_list)
# [10, 20, 40, 50, 30, 20]
print('----------------------------')

# 3. del statement
d_list = [10, 20, 30, 40, 50]
del d_list[1]
# Deletes the element at index 1 (20)
print(d_list)
# Output: [10, 30, 40, 50]
del d_list[1:3]
# Removes elements from index 1 to 2 ([30, 40])
print(d_list)
# [10, 50]
