# 0. Empty
my_tuple0 = ()

# 1. Parentheses
my_tuple1 = (1,2,3, "banana", "orange")

# 2. tuple() Constructor
my_tuple2 = tuple(["le", "vinh", 'chi', 2024 ])

# 3. tuple packing
item1 = 'apple'
item2 = 'orange'

my_tuple3 = item1, item2

# 4. Generator Expression
my_tuple4 = tuple(x*x for x in range(10))

# 5.Single-Element Tuple (Note the Comma)
single_element_tuple = (42,)

print("tuple 0:",my_tuple0)
print("tuple 1:",my_tuple1)
print("tuple 2:",my_tuple2)
print("tuple 3:",my_tuple3)
print("tuple 4:",my_tuple4)
print('Single Element:', single_element_tuple, ' _ type:', type(single_element_tuple))

