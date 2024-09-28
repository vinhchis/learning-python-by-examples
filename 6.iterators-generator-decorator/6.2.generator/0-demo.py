def my_generator():
    yield 1 # call next() - 1
    yield 2 # call next() - 2
    yield 4 # call next() - 3
    yield 5 # call next() - 4

g = my_generator()
print(next(g))
print(next(g))
print('---------------')

for n in g:
    print(n)

print(type(g))  