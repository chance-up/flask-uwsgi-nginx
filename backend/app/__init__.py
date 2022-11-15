from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request
from app.views import namespace_view, temp_view


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.register_blueprint(namespace_view.bp)
# app.register_blueprint(temp_view.bp)


  
