from flask import Flask
from flask_migrate import Migrate

from auth.auth import bl_auth
from profile.profile import bl_profile
from post.post import bl_post
from models import db
import os

app = Flask(__name__)
app.register_blueprint(bl_auth)
app.register_blueprint(bl_profile)
app.register_blueprint(bl_post)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = 'BLABLASECRET'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
