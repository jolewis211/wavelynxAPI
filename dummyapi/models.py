from app import db

class ApiKey(db.Model):
    key = db.Column(db.String(255), primary_key=True)

    def __init__(self, key):
        self.key = key

    def json(self):
        return {'key': self.key}