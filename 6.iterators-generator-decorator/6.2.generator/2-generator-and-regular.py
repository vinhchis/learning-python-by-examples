import timeit

def get_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def generate_squares(n):
    for i in range(n):
        yield i**2

n = 100000

# print("regular:", get_squares(n))
# print("generator:",list(generate_squares(n)))

# time
t1 = timeit.timeit(f'get_squares({n})', globals=globals(), number=1)
t2 = timeit.timeit(f'generate_squares({n})', globals=globals(), number=1)
print('generate_squares fasted than get_squares:', int(t1/t2))


