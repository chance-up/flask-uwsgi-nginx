from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request
from app.views import resources_view, connection_view


app = Flask(__name__)
CORS(app)
app.register_blueprint(resources_view.bp)
app.register_blueprint(connection_view.bp)
# app.register_blueprint(temp_view.bp)


  
