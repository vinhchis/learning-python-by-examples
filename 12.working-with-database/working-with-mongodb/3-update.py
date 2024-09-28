from pymongo import MongoClient
# allow display (Dict) as same as mongo pretty() (JSON)
import pprint


client = MongoClient('localhost', 27017)
db = client['library']
library_details = db['library_details']

myquery = {"book_name": "Python Programming"}
updatevalue = {"$set": {"volume": 10}}
library_details.update_one(myquery, updatevalue)
for lib in library_details.find():
    print(lib)
