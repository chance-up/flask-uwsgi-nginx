from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request
from app import ssh

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
  
@app.route('/api')
def index():
    return "Hello World!"

@app.route('/api/a')
def index1():
    result = ssh.dfh()
    return result


@app.route('/api/ab')
def index2():
    return "Hello World ab!"



# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def hello_pybo():
#         return 'Hello, Pybo!'

#     return app