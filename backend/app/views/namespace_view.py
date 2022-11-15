from flask import Blueprint
from app import ssh

bp = Blueprint('main', __name__, url_prefix='/api/namespace')


@bp.route('/getAll')
def getAllNamespace():
    result = ssh.getAllNamespace()

    
    return result

