from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Token(db.Model):
    __tablename__ = "tokens"
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    token = db.Column(db.String(32), nullable=False, unique=True)
