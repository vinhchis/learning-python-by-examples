from pymongo import MongoClient
# allow display (Dict) as same as mongo pretty() (JSON) 
import pprint

client = MongoClient('localhost',27017)
db = client['library']
library_details = db['library_details']

def display(dicts):
    for item in dicts:
        pprint.pprint(item)

# 1. Find one
# pprint.pprint(library_details.find_one())

# 2. find all
dicts = library_details.find({})
display(dicts)
print('--------------------------------')

# 3. Filter
# 3.1. book has book_author is 'Wes Mckinney'
book_author = 'Wes Mckinney'
dicts = library_details.find({'book_author': book_author})
# display(dicts)

# 3.2. book has book_name contains 'Data'
regex = "Data"
dicts = library_details.find({'book_name': {'$regex': regex}})
# display(dicts)

# 3.3. book has volume greater than 2
dicts = library_details.find({'volume': {'$gt': 2}})
# display(dicts)

# 4. sort in descending order of book_name
dicts = library_details.find().sort("book_name",-1)
display(dicts)
