import pymongo
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime as d

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
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    
    mycol = get_db_connection()

    posts = mycol.find()
    
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    
    post = get_post(post_id)
    
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        register = request.form['register']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        salary = float(request.form['salary'])
        work_month = float(request.form['work_month'])
        print(salary)

        if not register:
            flash('Register is required!')
        else:
           
            mycol = get_db_connection()
                        
            doc = { 
                "created" : d.now(),
                "name" : { "first_name" : firstname, 
                           "last_name" : lastname
                         }, 
                "register_num" : register,            
                "Эрүүл мэнд, нийгмийн даатгалын шимтгэл" : {
                    "Хөдөлмөрийн хөлс,түүнтэй адилтгах орлого /төгрөг/" : salary, 
                    "НДШ хувь хэмжээ": 25, 
                    "Ногдуулсан шимтгэл/төгрөг/ - Нийт дүн": salary * 25 / 100, 
                    "Ажил олгогчийн төлөх хувь хэмжээ" : 13.5,
                    "Үүнээс : Ажил олгогч" : salary * 0.135, 
                    "Даатгуулагчийн төлөх хувь хэмжээ" : 11.5, 
                    "Үүнээс : Даатгуулагч" : salary * 0.115            
                }, 
                "Татварын тооцоолол жилээр" : {
                    "Жилийн нийт орлого" : salary * work_month, 
                    "Орлого хүлээн авсан сарын тоо /ажилласан сар/" : work_month, 
                    "Сарын дундаж" : salary, 
                    "ЭМД, НДШ Хувь" : 11.5, 
                    "ЭМД, НДШ Дүн" :  salary * work_month * 11.5 /100, 
                    "Татвар ногдуулах орлого" : salary * work_month * (1 - 11.5 /100), 
                    "Ногдуулсан татварын хувь хэмжээ" :	10,
                    "Ногдуулсан татвар" :	 salary * work_month * (1 - 11.5 /100) * 0.10, 
                    "Хуулийн 23.1-т заасан хөнгөлөлт сард ногдох" :	18000,
                    "Хуулийн 23.1-т заасан хөнгөлөлт нийт" : 18000 * work_month,
                    "Хөнгөлөлтийн дараах татварын дүн" :	 salary * work_month * (1 - 11.5 /100) - 18000 * work_month,
                    "Хуулийн 7.1.6-д заасан орлогод ногдуулсан дүн" :	0,
                    "Нийт суутгуулсан албан татварын дүн" :	 salary * work_month * (1 - 11.5 /100) - 18000 * work_month             
                }
	        }
    
            # doc = {"name": "John", "age": i}
            mycol.insert_one(doc)
            return redirect(url_for('index'))
    return render_template('create.html')