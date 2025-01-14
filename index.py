from flask import Flask
from flask import request, session , make_response
from pymongo import MongoClient
from flask import Flask, request, jsonify, send_file
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import datetime
from datetime import datetime
import random
import json
from email.mime.text import MIMEText
import smtplib
import uuid
import re
import os
import requests
from io import BytesIO
import subprocess
import jwt
import threading
import multiprocessing
import time
import requests
import base64


app = Flask(__name__)
CORS(app)

client = MongoClient(
    'mongodb+srv://bnbdevs:feLC7m4jiT9zrmHh@cluster0.fjnp4qu.mongodb.net/?retryWrites=true&w=majority')
app.config['MONGO_URI'] = 'mongodb+srv://bnbdevs:feLC7m4jiT9zrmHh@cluster0.fjnp4qu.mongodb.net/?retryWrites=true&w=majority'
db = client['sat_db']

host = ""


# notificationFlag = True

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home():
    return 'home page'


#-----------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ------------------------------------------------------------------------------------------------------------


@app.route("/getSensorData", methods=["GET"])
def getSensorData():
    satData_db = db["satData_db"]
    dt = []
    dt = list(satData_db.find({},{'_id':0}))
    return jsonify({"data":dt})

@app.route("/sendData", methods=["GET"])
def sendData():
    satData = db["satData"]
    ans = []
    ans = list(satData.find({"status": {"$ne": "Active"}}, {"_id": 0}))
    return jsonify({"success":True})


@app.route('/updateData', methods=['GET'])
def update_data():
    return "Ok"




if __name__ == '__main__':
    app.run(host="0.0.0.0")





