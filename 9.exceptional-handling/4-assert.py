def divide(a, b): 
    assert b != 0, "Cannot divide by zero" 
    return a / b 
 
result = divide(10, 2)  # This is valid 
print(result) 
 
result = divide(10, 0)  # This will raise an AssertionError 
print(result) 
# AssertionError: Cannot divide by zero