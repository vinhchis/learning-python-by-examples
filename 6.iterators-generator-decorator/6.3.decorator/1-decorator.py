#Decorator to Calculate execution time of a function
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time-start_time:.4f} seconds to execute")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(2)
    print("Function execution complete")

slow_function()

