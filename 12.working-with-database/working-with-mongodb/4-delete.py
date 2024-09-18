from pymongo import MongoClient
# allow display (Dict) as same as mongo pretty() (JSON) 
import pprint

client = MongoClient('localhost',27017)
db = client['library']
library_details = db['library_details']

myquery = {"book_author":"David Beazley"}
library_details.delete_one(myquery)
for lib in library_details.find():
    print(lib)