import json

serialized_data = {}
with open("./data/document.json", "r") as file: 
    serialized_data = file.read() 
 

# Deserialize the JSON data back into a Python dictionary 
deserialized_data = json.loads(serialized_data) 
 
# Print the deserialized data 
print("Deserialized Data:", deserialized_data)
print('Type:', type(deserialized_data)) 
 
# Access specific values in the dictionary 
print("Name:", deserialized_data["name"]) 
print("Age:", deserialized_data["age"]) 
print("City:", deserialized_data["city"]) 