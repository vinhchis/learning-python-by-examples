#  pop(key, default=None)
# Generating a dictionary by some key-value pairs
student_scores = {
    "Luis": 95,
    "Carlos": 88,
    "Isabella": 92
}
# Using the pop() method to retrieve and remove values based on keys
# Removing and getting the value for "Luis"
luis_score = student_scores.pop("Luis")

# Removing and getting the value for "Diego" (with default)
diego_score = student_scores.pop("Diego", 0)

# Printing the removed values and the updated #dictionary
print("Luis's score:", luis_score)
print("Diego's score (with default):", diego_score)
print("Updated student scores dictionary:", student_scores)

# Output:
# Luis's score: 95
# Diego's score (with default): 0
# Updated student scores dictionary: {'Carlos': 88, 'Isabella': 92}