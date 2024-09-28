# serialization from dictionary to JSON
import json 
 
# Sample data in a Python dictionary 
data = { 
    "name": "John", 
    "age": 30, 
    "city": "New York" 
} 
 
# Serialize the data to JSON format 
serialized_data = json.dumps(data, indent=4) 
 
# Print the serialized data 
print("Serialized Data:", serialized_data) 
print("Type:",type(serialized_data)) 
 
# Save the serialized data to a file 
with open("./data/document.json", "w") as file: 
    file.write(serialized_data) 
 
print("Data saved to 'data.json' file.") 