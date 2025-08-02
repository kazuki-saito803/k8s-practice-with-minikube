from flask import Flask, request, jsonify
import os

app = Flask(__name__)

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

@app.route("/")
def home():
    user = request.authorization
    if user and user.username == USERNAME and user.password == PASSWORD:
        return "Hello World with authentication", 200
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)