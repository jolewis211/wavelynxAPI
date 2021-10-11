import string
import random
import json
from flask import request, jsonify, Blueprint
from models import Token, db

app_router = Blueprint('workouts', __name__, url_prefix='')


def generateToken():
    """
    Generates a random token with a length that is > 8 and < 32.
    """
    length = random.randint(8, 32)
    rdmtoken = ''.join(random.choice(string.printable) for i in range(length))
    return f'{rdmtoken}'


@app_router.route('/token', methods=['GET'])
def token():
    '''
    Returns a valid 8-32 character random token in json format.
    '''
    currToken = generateToken()
    if len(currToken) >= 8 or len(currToken) <= 32:
        db.session.add(Token(token=f'{currToken}'))
        db.session.commit()
    return jsonify(
        token=currToken,
        status='Success! Token was generated'), 200


@app_router.route('/verify', methods=['POST'])
def verifyToken():
    """
    Verifies if a provided token was previously generated.
    """
    if request:
        data = json.dumps(request.json)
        reqToken = json.loads(data)["token"]
        if len(reqToken) >= 8 and len(reqToken) <= 32:
            found = Token.query.filter(Token.token == f'{reqToken}').first()
            print(found)
            if found:
                message = "Success! It's an older code, sir, but it checks out."  # noqa
            else:
                message = "Code not found."
        else:
            message = 'Invalid token length.'
    else:
        message = 'Invalid JSON request'
    return jsonify(status=message)
