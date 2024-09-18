# Taking input from the user as a comma-separated #string
input_string = input("Enter a number list separated by commas:")
# Splitting the input string and converting it into #a list of integers
input_list = [int(x) for x in input_string.split(',')]
print("Input list:", input_list)
