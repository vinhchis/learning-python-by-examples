def my_generator():
    yield 1
    yield 2
    yield 4
    yield 5

g = my_generator()
print(next(g))
print(next(g))
print('---------------')

for n in g:
    print(n)

print(list(g))  