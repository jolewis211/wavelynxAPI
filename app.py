from flask_api import status
import dummyapi.token as token
from dummyapi import app, db
from dummyapi.models import ApiToken

# I'd like to keep deployment as-is 
# with this decorator, users do not need to build the db from CLI
@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/token", methods=["GET"])
def get_token():
    """
    Generate and store a new token.
    """
    new_token: str = token.generate_token()
    api_obj = ApiToken(new_token)
    db.session.add(api_obj)
    db.session.commit()

    return (
        {"status": "success", 
        "message": "new token generated",
        "token": new_token},
        status.HTTP_201_CREATED
    )


@app.route("/verify/<string:token>", methods=["POST"])
def verify_token(token):
    """
    Verify that the provided token has been previously generated.
    """
    results = ApiToken.query.filter_by(token=token).all()
    if results:
        return (
            {"status": "success",
            "message": f"{token} is a registered token"},
            status.HTTP_202_ACCEPTED
        )
    else:
        return (
            {"status": "unathorized",
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
