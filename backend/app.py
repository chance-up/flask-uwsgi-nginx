from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
  
@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)