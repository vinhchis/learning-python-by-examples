# Decorator to convert input arguments to uppercase
def uppercase_args(func):
    def wrapper(*args, **kwargs):
        modified_args = [arg.upper() if isinstance(arg,str) else arg for arg in args]
        result = func(*modified_args, **kwargs)
        return result
    return wrapper

@uppercase_args
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
print(greet("Bob"))