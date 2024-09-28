class LogFunctionCall:
    def __init__(self, func):
       self.func = func 

    # implement __call__  method
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with args: {args}, kwargs: {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} returned: {result}")
        return result

@LogFunctionCall
def add(a, b):
    return a + b

result = add(3, 5)