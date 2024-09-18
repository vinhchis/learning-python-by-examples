from pymongo import MongoClient
import re

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

# Basic regex query
results = collection.find({'field': {'$regex': 'pattern'}})

# Case-insensitive match
results = collection.find({'field': {'$regex': 'pattern', '$options': 'i'}})

# Starts with
results = collection.find({'field': {'$regex': '^start'}})

# Ends with
results = collection.find({'field': {'$regex': 'end$'}})

# Contains
results = collection.find({'field': {'$regex': 'contains'}})

# Using re.compile()
pattern = re.compile('pattern', re.IGNORECASE)
results = collection.find({'field': pattern})

# Combining with other query operators
results = collection.find({
    'field': {'$regex': 'pattern', '$options': 'i'},
    'anotherField': {'$gt': 100}
})

# Example: Find documents where the name starts with 'John'
results = collection.find({'name': {'$regex': '^John'}})

# Example: Find documents where the email contains 'example.com', case-insensitive
results = collection.find({'email': {'$regex': 'example\.com', '$options': 'i'}})

# Iterate through results
for doc in results:
    print(doc)