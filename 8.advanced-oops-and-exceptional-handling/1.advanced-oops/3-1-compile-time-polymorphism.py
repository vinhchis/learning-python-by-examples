# compile-time (or Static) polymorphism -> overloading
class MathOperations:
    def add(self, a=None, b=None, c=None):
        if c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0


# Create an instance of the MathOperations class
math = MathOperations()

# Method overloading using default arguments
print(math.add())          # Output: 0
print(math.add(5))         # Output: 5
print(math.add(5, 10))     # Output: 15
print(math.add(5, 10, 20))  # Output: 35
