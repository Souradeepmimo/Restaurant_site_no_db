from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from flask_session import Session
import pymongo
import json
from flask import render_template,redirect,url_for
from flask import Flask, request, render_template,redirect,url_for,flash,session
app=Flask(__name__)

myclient            =  pymongo.MongoClient("mongodb://localhost:27017/")
mydb                =  myclient['Template']
Restaurant          =  mydb['Restaurant']

@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/insert",methods=['POST'])
def insert():
    if request.method=='POST':
        _json     =  request.form
        Name      =  _json['name']
        Email     =  _json['email']
        Phone     =  _json['phone']
        Date      =  _json['date']
        Time      =  _json['time']
        People    =  _json['people']
        Message   =  _json['message']

        if Name and Email and Phone and Date and Time and People and Message:
            Restaurant.insert_one({'name':Name,'email':Email,'phone':Phone,'date':Date,'time':Time,'people':People,'message':Message})
            return 'OK',200

app.run()
