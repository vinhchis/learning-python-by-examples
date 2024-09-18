# A deep copy of a dictionary creates a completely independent copy of both the outer dictionary and all the nested objects it contains.
import copy
original_dict = {
    "nested_dict": {"key": "value"},
    "list": [1, 2, 3]
}

# Deep copy using deepcopy() function
deep_copied_dict = copy.deepcopy(original_dict)

# change original
original_dict['list'].append(20)

# change deep copied 
deep_copied_dict['list'] = ["it", "is" , "deep"]

print("original dict:", original_dict)
print("deep copied dict:", deep_copied_dict)
# original dict: {'nested_dict': {'key': 'value'}, 'list': [1, 2, 3, 20]}
# deep copied dict: {'nested_dict': {'key': 'value'}, 'list': ['it', 'is', 'deep']}