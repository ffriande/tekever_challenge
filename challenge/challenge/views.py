from flask import Blueprint, request

main = Blueprint('main', __name__)

    
@main.route('/')
def index():
    return 'Hello World!'


@main.route('/create_account', methods=['POST'])
def create_account():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'
    return 