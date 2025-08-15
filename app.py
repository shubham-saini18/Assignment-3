from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "mongodb+srv://admin:admin@cluster0.djhrcyo.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["test_database"]
collection = db["test_collection"]

# API Route
@app.route("/api", methods=["GET"])
def get_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404

#  Form Route 
@app.route("/form", methods=["GET", "POST"])
def form():
    error_message = None
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            if not name or not email:
                raise ValueError("Name and Email are required.")

            # Check if email already exists
            existing_user = collection.find_one({"email": email})
            if existing_user:
                raise ValueError("Email already exists in database.")

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            return redirect(url_for("success"))
        except Exception as e:
            error_message = str(e)

    return render_template("form.html", error=error_message)

#  Success Route 
@app.route("/success")
def success():
    return render_template("success.html")

#  Main 
if __name__ == "__main__":
    app.run(debug=True)
