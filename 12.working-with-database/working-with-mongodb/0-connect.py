from pymongo import MongoClient

client = MongoClient() # connect to localhost and port 27017

db = client.portfolio # create portfolio database
investments = db.investments # create investment collection

# command above use lazily -> only run when operators were used (create, read, update, delete)
print("Connected to MongoDB")