import numpy as np
from pymongo import MongoClient
from flask import Flask, request, render_template
from functions import get_json

app = Flask(__name__)

myClient = MongoClient('mongodb+srv://obajone:obajone@cluster0.cfkma.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = myClient.Chokhmah

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/', methods = ["POST", "GET"])
def employee():
    json = get_json()
    db.Teachers_ID.insert_one(json)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)