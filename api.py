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
Restaurant_message  =  mydb['Restaurant_message']

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

@app.route("/insertmessage",methods=['POST'])
def insertmessage():
    if request.method=='POST':
        _json        =  request.form
        Name         =  _json['name']
        Email        =  _json['email']
        Subject      =  _json['subject']
        Message      =  _json['message']
        #Time      =  _json['time']
        #People    =  _json['people']
       # Message   =  _json['message']

        if Name and Email and Subject and Message :
            Restaurant_message.insert_one({'name':Name,'email':Email,'subject':Subject,'message':Message})
            return 'OK',200

app.run()
