my_list = (1, 2, 4, 5, 6)
mi = iter(my_list)
print(next(mi))
print(next(mi))
print(next(mi))
print(next(mi))

print(type(mi))
# 1
# 2
# 4
# 5
# <class 'tuple_iterator'>