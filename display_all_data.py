import pymongo
from flask import Flask, render_template


# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database object
mydb = client["mydatabase"]

app = Flask(__name__)

@app.route('/')
def home():
    
    # Create a collection object
    mycol = mydb["mycollection"]

    documents = mycol.find()
    return render_template('index.html', documents=documents)

if __name__ == '__main__':
    app.run()


