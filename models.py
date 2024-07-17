from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(120))
    password = db.Column(db.String(128))

    def password_setter(self, password_):
        self.password = generate_password_hash(password_)

    def verify_password(self, password_):
        return check_password_hash(self.password, password_)
