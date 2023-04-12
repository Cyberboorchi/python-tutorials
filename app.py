import pymongo
from flask import Flask, render_template
from werkzeug.exceptions import abort


def get_db_connection():
    # Establish a connection to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Create a database object
    mydb = client["mydatabase"]        
    
    # Create a collection object
    mycol = mydb["mycollection"]
    return mycol

def get_post(post_id):
    mycol = get_db_connection()
    myquery = { "_id": post_id }
    
    post = mycol.find_one(myquery)
    
    if post is None:
        abort(404)
    return post


app = Flask(__name__)

@app.route('/')
def index():
    
    mycol = get_db_connection()

    posts = mycol.find()
    
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    
    post = get_post(post_id)
    
    return render_template('post.html', post=post)

