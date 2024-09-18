def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Calling the function using positional arguments
describe_person("Alice", 30, "New York")
# Calling the function using keyword arguments
describe_person(age=25, city="Los Angeles", name="Bob")
# Output:
# Alice is 30 years old and lives in New York.
# Bob is 25 years old and lives in Los Angeles.
