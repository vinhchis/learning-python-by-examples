def get_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def generate_squares(n):
    for i in range(n):
        yield i**2

print("regular:", get_squares(5))

square_gen = generate_squares(5)

print("generator:" , end = ' ' )
for num in square_gen:
    print(num, end=', ')