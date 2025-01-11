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

#--------------------------------------------------------------------------------

# file_dir = "/home/bnbdevelopers-files/htdocs/files.bnbdevelopers.in/mcf_files/"
# files_url = "https://files.bnbdevelopers.in"
# files_base_dir = "/home/bnbdevelopers-files/htdocs/files.bnbdevelopers.in/"
# files_base_url = "https://files.bnbdevelopers.in/mcf_files/"

file_dir = "/home/mcfcamp-files/htdocs/files.mcfcamp.in/mcf_files/"
files_url = "https://files.mcfcamp.in"
files_base_dir = "/home/mcfcamp-files/htdocs/files.mcfcamp.in/"
files_base_url = "https://files.mcfcamp.in/mcf_files/"

#----------------------------------------------------------------------------------



app = Flask(__name__)
CORS(app)

client = MongoClient(
    'mongodb+srv://bnbdevs:feLC7m4jiT9zrmHh@cluster0.fjnp4qu.mongodb.net/?retryWrites=true&w=majority')
app.config['MONGO_URI'] = 'mongodb+srv://bnbdevs:feLC7m4jiT9zrmHh@cluster0.fjnp4qu.mongodb.net/?retryWrites=true&w=majority'

# client = MongoClient(
#     'mongodb+srv://mcfcamp:mcf123@mcf.nyh46tl.mongodb.net/')
# app.config['MONGO_URI'] = 'mongodb+srv://mcfcamp:mcf123@mcf.nyh46tl.mongodb.net/'

app.config['SECRET_KEY'] = 'a6d217d048fdcd227661b755'
db = client['sat_db']
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "ic2023wallet@gmail.com"
app.config['MAIL_PASSWORD'] = "irbnexpguzgxwdgx"

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

@app.route("/sendData", methods=["POST"])
def sendData():
    satData = db["satData"]
    ans = []
    ans = list(satData.find({"status": {"$ne": "Active"}}, {"_id": 0}))
    return jsonify({"success":True})


@app.route('/updateData', methods=['PUT'])
def update_discount():
    try:
        data = request.get_json()

        satData_db = db["satData_db"]
        dt = satData_db.find_one({"selector": data['selector']})

        if not dt:
            return jsonify({"error": f"No data found"}), 404  # Not Found

        # Update the discount_code of the discount
        satData_db.update_one({"selector": data['selector']}, {"$set": {"data": data['data']}})

        return jsonify({"success": f"True"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error



if __name__ == '__main__':
    app.run(host="0.0.0.0")





