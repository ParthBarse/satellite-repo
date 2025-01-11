from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import datetime
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# MongoDB client setup
client = MongoClient(
    'mongodb+srv://bnbdevs:feLC7m4jiT9zrmHh@cluster0.fjnp4qu.mongodb.net/?retryWrites=true&w=majority'
)
db = client['sat_db']

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
    return 'home page'

@app.route("/getSensorData", methods=["GET"])
def getSensorData():
    satData_db = db["satData_db"]
    dt = list(satData_db.find({}, {'_id': 0}))
    return jsonify({"data": dt})

@app.route("/sendData", methods=["POST"])
def sendData():
    satData = db["satData"]
    ans = list(satData.find({"status": {"$ne": "Active"}}, {"_id": 0}))
    return jsonify({"success": True})

@app.route('/updateData', methods=['PUT'])
def update_discount():
    try:
        data = request.get_json()
        satData_db = db["satData_db"]
        dt = satData_db.find_one({"selector": data['selector']})

        if not dt:
            return jsonify({"error": "No data found"}), 404  # Not Found

        satData_db.update_one(
            {"selector": data['selector']},
            {"$set": {"data": data['data']}}
        )
        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

# Vercel's handler for serverless functions
def handler(event, context):
    from flask_lambda import FlaskLambda
    return FlaskLambda(app)(event, context)
