# A shallow copy of a dictionary creates a new dictionary object, 
# but it does not create new copies of the nested objects -> references nested objects

original_dict = {
    "nested_dict": {"key": "value"},
    "list": [1, 2, 3]
}

# 1.Shallow copy using copy() method
shallow_copied_dict = original_dict.copy()


# 2. Shallow copy using dict() constructor 
# shallow_copied_dict = dict(original_dict)

# change nested object in original dictionary
shallow_copied_dict['list'].append(10)

print("original dict:", original_dict)
print("shallow copied dict:", shallow_copied_dict)
# original dict: {'nested_dict': {'key': 'value'}, 'list': [1, 2, 3, 10]}
# shallow copied dict: {'nested_dict': {'key': 'value'}, 'list': [1, 2, 3, 10]}