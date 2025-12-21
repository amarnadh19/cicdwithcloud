# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, Docker!</h1>'

if __name__ == "__main__":
    # The application runs on port 8000 inside the container
    app.run(host="0.0.0.0", port=8080)
