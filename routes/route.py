from flask import Blueprint
from controllers.controller import index, upload

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/', methods=['POST'])(upload)