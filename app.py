from flask_api import FlaskAPI, status
import dummyapi.token as token

app = FlaskAPI(__name__)
app.tokens = []


@app.route("/token", methods=["GET"])
def get_token():
    """
    Generate and store a new token.
    """
    new_token: str = token.generate_token()
    app.tokens.append(new_token)
    return {"status": "success", "token": new_token}


@app.route("/verify", methods=["POST"])
def verify_token():
    """
    Verify that the provided token has been previously generated.
    """
    return (
        {"status": "not implemented"},
        status.HTTP_400_BAD_REQUEST,
    )


@app.route(
    "/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]
)
def catch_all(path):
    """
    Return errors for all invalid paths or request methods.
    """
    return (
        {"status": "error"},
        status.HTTP_404_NOT_FOUND,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
