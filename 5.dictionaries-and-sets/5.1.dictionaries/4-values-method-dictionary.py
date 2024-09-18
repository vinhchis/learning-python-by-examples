# Generating a dictionary by some key-value pairs
student_scores = {
"Elena": 95,
"Javier": 88,
"Luisa": 92
}

# Using the values() method to retrieve and print the #values
all_scores = student_scores.values()
# Converting the values view into a list for 
# demonstration purposes
score_list = list(all_scores)
# Printing the list of values
print("List of scores:", score_list)