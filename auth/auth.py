from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User, db
bl_auth = Blueprint('auth', __name__, template_folder='templates')


@bl_auth.route('/login', methods=['GET', 'POST'])
def login():
    template = 'auth/login.html'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                session['email'] = user.email
                return redirect(url_for('profile.profile'))
            else:
                flash("Неверный пароль или email")
                return redirect(url_for('auth.login'))
        else:
            flash("Такого пользователя не существует")
            return redirect(url_for('auth.login'))

    return render_template(template)


@bl_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    template = 'auth/signup.html'
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_submit = request.form['password_submit']
        if password != password_submit:
            flash('Passwords do not match')
            return redirect(url_for('auth.signup'))
        else:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template(template)


@bl_auth.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('profile.profile'))
