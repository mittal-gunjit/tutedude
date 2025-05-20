from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)

connection_string = os.getenv("MONGODB_URI")
client = MongoClient(connection_string)
db = client["experiment"]
collection = db["experiment"]

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = dict(request.json)
        # raise AssertionError("This is a test error")  # uncomment this line to test error handling
        print("Received data:", data)
        collection.insert_one(data)
        return "Data submitted successfully!"
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}, 500

@app.route("/view")
def api():
    data = collection.find()
    data_list = []
    for item in data:
        item.pop("_id", None)  # Remove the MongoDB ObjectId field
        data_list.append(item)
    # data = list(data)
    
    print("Data from MongoDB:", data_list)
    return {"data": data_list}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)