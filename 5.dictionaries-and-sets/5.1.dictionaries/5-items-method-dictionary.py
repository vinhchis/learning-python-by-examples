# Generating a dictionary by some key-value pairs
student_scores = {
    "John": 95,
    "James": 88,
    "Robert": 92
}
# Using the items() method to retrieve and print the key-#value pairs
all_student_info = student_scores.items()

# Converting the items view into a list of tuples for
# demonstration purposes
student_info_list = list(all_student_info)

# Printing the list of key-value pairs
print("List of student information:", student_info_list)
# [('John', 95), ('James', 88), ('Robert', 92)]