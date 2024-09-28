from pymongo import MongoClient
# allow display (Dict) as same as mongo pretty() (JSON) 
import pprint

DB_CONFIG = {
    'host' : 'localhost',
    'port' : 27017
}

client = MongoClient(**DB_CONFIG)
db = client['library']
library_details = db['library_details']

def insert():
    lib = [
        {"book_id": "1010", "book_name": "Python Programming", "book_author": "John M Zelle",
        "volume": 3},
        {"book_id": "1019", "book_name": "Python for Data Analysis", "book_author": "Wes Mckinney",
            "volume": 1},
        {"book_id": "1009", "book_name": "Python Cookbook", "book_author": "David Beazley",
            "volume": 3}
    ]
    library_details.insert_many(lib)
    print("Documents Inserted successfully")


def display(dicts):
    for item in dicts:
        pprint.pprint(item)

# 0 . insert
# insert()


# 1. Find one
# pprint.pprint(library_details.find_one())

# 2. find all
dicts = library_details.find({})
display(dicts)

# 3. Filter
# 3.1. 
book_author = 'Wes Mckinney'
dicts = library_details.find({'book_author': book_author})
# display(dicts)

# 3.2.
regex = "Data"
dicts = library_details.find({'book_name': {'$regex': regex}})
# display(dicts)

# 3.3
dicts = library_details.find({'volume': {'$gt': 2}})
# display(dicts)
