import pickle

data = { 
    "name": "John", 
    "age": 30, 
    "city": "New York" 
} 
 
# Serialize the data to binary
serialized_data = pickle.dumps(data)
 
# Print the serialized data 
print("Serialized Data:", serialized_data) 
print("type:",type(serialized_data)) 
 
# Save the serialized data to a file 
with open("./data/document.bin", "wb") as file: 
    file.write(serialized_data) 
 
print("Data saved to 'data.json' file.") 