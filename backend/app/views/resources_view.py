from flask import Blueprint
from app import ssh


bp = Blueprint('main', __name__, url_prefix='/api/resources')

@bp.route('/getClusterInfo')
def getClusterInfo():
    result = ssh.getClusterInfo()
    return result


@bp.route('/getAll')
def getAllNamespace():
    result = ssh.getAllNamespace()
    return result

