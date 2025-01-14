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
    try:
        # Extract all query parameters dynamically
        query_params = request.args.to_dict()

        # Validate that query parameters are provided
        if not query_params:
            return jsonify({"error": "No query parameters provided"}), 400  # Bad Request

        # Access the database collection
        satData_db = db["satData_db"]

        # Iterate over the query parameters and update each corresponding document
        for selector, value in query_params.items():
            # Find the document with the matching selector
            dt = satData_db.find_one({"selector": selector})
            
            if not dt:
                # Skip updating if no matching document is found
                continue

            # Update the document with the new value
            satData_db.update_one({"selector": selector}, {"$set": {"data": value}})

        return jsonify({"success": True, "updated_selectors": list(query_params.keys())})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error




@app.route('/updateSensorData', methods=["GET"])
def update_sensor_data():
    return jsonify({"msg":"success"})




if __name__ == '__main__':
    app.run(host="0.0.0.0")





