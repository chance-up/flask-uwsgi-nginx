from flask import Blueprint
from app import ssh

bp = Blueprint('main', __name__, url_prefix='/api')


@bp.route('/')
def index():
    return "Hello World!"

@bp.route('/a')
def index1():
    result = ssh.getAllPod()
    return result


@bp.route('/ab')
def index2():
    return "Hello World ab!"

@bp.route('/abc')
def hello_pybo():
    return "Hello World abc!"
