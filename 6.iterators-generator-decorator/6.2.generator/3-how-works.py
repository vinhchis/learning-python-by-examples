def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
countdown_gen = countdown_generator(5)
print(next(countdown_gen))  # Pauses at yield, prints 5
print(next(countdown_gen))  # Resumes from where it paused, prints 4
print(next(countdown_gen))  # Resumes again, prints 3
