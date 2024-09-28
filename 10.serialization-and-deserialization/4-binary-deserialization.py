import pickle
 
# Sample serialized data in JSON format . Use ''' to create a paragraph
serialized_data = {}
with open("./data/document.bin", "rb") as file: 
    serialized_data = file.read() 
 

# Deserialize the JSON data back into a Python dictionary 
deserialized_data = pickle.loads(serialized_data) 
 
# Print the deserialized data 
print("Deserialized Data:", deserialized_data, ',type:', type(deserialized_data)) 
 
# Access specific values in the dictionary 
print("Name:", deserialized_data["name"]) 
print("Age:", deserialized_data["age"]) 
print("City:", deserialized_data["city"]) 