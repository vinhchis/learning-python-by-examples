# Generating a dictionary by some key-value pairs
student_scores = {
"Emily": 95,
"James": 88,
"Sophia": 92
}
# Iterating through keys using a loop
print("Iterating through keys:")
for student_name in student_scores:
    print(student_name)
    
# Iterating through values using a loop
print("\nIterating through values:")
for score in student_scores.values():
    print(score)

# Iterating through key-value pairs using a loop
print("\nIterating through key-value pairs:")
for student_name, score in student_scores.items():
    print(student_name, ":", score)