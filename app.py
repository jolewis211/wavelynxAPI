from flask_api import FlaskAPI, status
import dummyapi.token as token
from flask_sqlalchemy import SQLAlchemy
import os

app = FlaskAPI(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'\
     + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# I'd like to keep deployment as-is 
# with this function users do not need to build the db from CLI
@app.before_first_request
def create_tables():
    db.create_all()


class ApiKey(db.Model):
    key = db.Column(db.String(255), primary_key=True)

    def __init__(self, key):
        self.key = key

    def json(self):
        return {'key': self.key}


@app.route("/token", methods=["GET"])
def get_token():
    """
    Generate and store a new token.
    """
    new_token: str = token.generate_token()
    api_obj = ApiKey(new_token)
    db.session.add(api_obj)
    db.session.commit()

    return {"status": "success", "token": new_token}


@app.route("/verify/<string:token>", methods=["POST"])
def verify_token(token):
    """
    Verify that the provided token has been previously generated.
    """
    results = ApiKey.query.filter_by(key=token).all()
    if results:
        return (
            {"status": "success",
            "message": f"{token} is a registered token"},
            status.HTTP_202_ACCEPTED
        )
    else:
        return (
            {"status": "success",
            "message": f"{token} is not a registered token"},
            status.HTTP_401_UNAUTHORIZED,
        )


@app.route(
    "/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]
)
def catch_all(path):
    """
    Return errors for all invalid paths or request methods.
    """
    if path == 'verify/':
        return (
        {"status": "error", 
        "message": "no token provided in verify endpoint"},
        status.HTTP_404_NOT_FOUND,            
        )

    return (
        {"status": "error",
        "message": "error"},
        status.HTTP_404_NOT_FOUND,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
