import click
from flask.cli import with_appcontext
from flask import Flask
from flask_migrate import Migrate
from routes import app_router  # noqa
from config import Config
from models import db

app = Flask(__name__)
app.register_blueprint(app_router)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)


@click.command(name='create')
@with_appcontext
def create():
    db.create_all()


app.cli.add_command(create)

if __name__ == "__main__":
    app.run(host="localhost", port=Config.FLASK_RUN_PORT)
