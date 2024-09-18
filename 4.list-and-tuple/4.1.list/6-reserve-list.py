# 1. reverse()
my_list1 = [1, 2, 3, 4, 5]
my_list1.reverse()
# Reverses the list in place
print('reverse list use reverse():',my_list1)
# Output: [5, 4, 3, 2, 1]

print('----------------')
# 2. slicing method
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
# Slicing with a step of -1
print("origin list:", my_list)
print("reverse list with slicing method:",reversed_list)
# Output: [5, 4, 3, 2, 1]