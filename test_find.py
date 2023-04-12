import pymongo
from flask import Flask, render_template
from werkzeug.exceptions import abort

    # Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Create a database object
mydb = client["mydatabase"]        
    
    # Create a collection object
mycol = mydb["mycollection"]

myquery = { "_id" : 5 }
    
post = mycol.find_one(myquery)
    
print(post)

if post is None:
    abort(404)
        