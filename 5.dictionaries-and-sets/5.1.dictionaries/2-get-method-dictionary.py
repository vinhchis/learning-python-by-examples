# Generating a dictionary by adding certain key-value #pairs.
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Carol": 92
}
# Using the get() method to retrieve scores
alice_score = student_scores.get("Alice")
# Returns 95 (key exists)

dave_score = student_scores.get("Dave")
# Returns None (key doesn't exist)

# Using the get() method with a default value
eve_score = student_scores.get("Eve", 0)
# Returns 0 (key doesn't exist, default provided)

# Printing the results
print("Alice's score:", alice_score)
print("Dave's score:", dave_score)
print("Eve's score:", eve_score)