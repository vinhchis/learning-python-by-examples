# Creating a dictionary of students with their in format as nested dictionaries
students = {
    "Emma": {
        "age": 20,
        "major": "Engineering",
        "grades": [85, 90, 78]
    },
    "Liam": {
        "age": 22,
        "major": "Business",
        "grades": [92, 88, 95]
    },
    "Olivia": {
        "age": 21,
        "major": "Computer Science",
        "grades": [75, 82, 79]
    }
}
# Accessing and manipulating nested dictionary values
emma_major = students["Emma"]["major"]  # Accessing Emma's #major
liam_grades = students["Liam"]["grades"]  # Accessing Liam's #grade
olivia_age = students["Olivia"]["age"]  # Accessing #Olivia's age
# Modifying nested dictionary values
students["Emma"]["grades"].append(88)  # Adding a new #grade for
# Emma
# Printing the updated information
print("Emma's major:", emma_major)
print("Liam's grades:", liam_grades)
print("Olivia's age:", olivia_age)
print("Updated grades for Emma:", students["Emma"]["grades"])
