# use if/else to raise errors
def divide(a, b): 
    if b == 0: 
        return "Error: Division by zero" 
    return a / b 
 
# Main program 
numerator = input("Enter the numerator: ") 
denominator = input("Enter the denominator: ") 
 
if not numerator.isdigit() or not denominator.isdigit(): 
    print("Error: Invalid input. Please enter valid numbers.") 
else: 
    numerator = float(numerator) 
    denominator = float(denominator) 
     
    result = divide(numerator, denominator) 
    print("Result:", result) 