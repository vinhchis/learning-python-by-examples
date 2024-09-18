# log information about function calls, arguments, and results without cluttering the actual function code
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        
        # Fixed the print statement
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3, 5)
#Output: Calling add with args: (3, 5), kwargs: {} add returned: 8