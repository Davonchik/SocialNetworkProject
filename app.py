from flask import Flask
from flask_migrate import Migrate

from auth.auth import bl_auth
from profile.profile import bl_profile
from post.post import bl_post
from models import db

app = Flask(__name__)
app.register_blueprint(bl_auth)
app.register_blueprint(bl_profile)
app.register_blueprint(bl_post)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost:5432/postgres'
app.config['SECRET_KEY'] = 'BLABLASECRET'
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
