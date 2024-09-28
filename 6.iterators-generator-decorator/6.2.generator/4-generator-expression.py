# the same list comprehension but use tuple instead of list
squares_generator = (x ** 2 for x in range(10))

for square in squares_generator:
    print(square)