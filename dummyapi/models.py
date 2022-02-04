from app import db

class ApiToken(db.Model):
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)
    token = db.Column(db.String(255))

    def __init__(self, key):
        self.token = key

    def json(self):
        return {'key': self.token}