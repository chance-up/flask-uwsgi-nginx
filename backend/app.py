from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
  
@app.route('/api')
def index():
    return "Hello World!"

@app.route('/api/a')
def index1():
    return "Hello World! a"


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5001)