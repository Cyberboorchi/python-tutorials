from pymongo import MongoClient

# connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# get all database names
db_names = client.list_database_names()

print(db_names)


client["mydatabase"]["mycollection"].delete_many({})

