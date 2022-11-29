from flask import Blueprint
from app import ssh

bp = Blueprint('connection', __name__, url_prefix='/api/connection')

@bp.route('/connect')
def connect():
    result = ssh.connect()
    print(result)
    return '{result : "true"}'


@bp.route('/disconnect')
def disconnect():
    result = ssh.disconnect()
    print(result)
    return '{result : "true"}'


