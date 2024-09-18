# 1. Square
square = lambda x : x*x

x = 10
result =square(10)
print(f'Square of {x} is {result}')
print('------------------------')
# 2. Iterate two list as a dictionary
names = ['chi', 'hoang', 'thao']
ages = [16, 20, 32]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index+1}. {name} is {age} years old.")
