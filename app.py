from flask import request

app = Flask(__name__)

@app.route('/create_account', methods=['POST']) 
def create_account():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json)
        return json
    else:
        return 'Content-Type not supported!'
    return 