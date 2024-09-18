import os
def read_and_divide(filename): 
    try: 
        with open(filename, 'r') as file: 
            numerator = float(file.readline()) 
            denominator = float(file.readline()) 
            result = numerator / denominator 
            return result 
    except FileNotFoundError: 
        print(f"Error: File '{filename}' not found.") 
    except ZeroDivisionError: 
        print("Error: Division by zero is not allowed.") 
    except ValueError: 
        print("Error: Invalid data in the file. Please ensure numeric values.") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
 
# Main program 
script_dir = os.path.dirname(os.path.abspath(__file__)) # get absolute path
print(f"Script directory: {script_dir}") 
# os.chdir(script_dir)  # change path working directory

file_name = input("Enter the name of the file: ") 
# TODO: modify relative path file
result = read_and_divide(file_name) 
if result is not None: 
    print("Result:", result) 