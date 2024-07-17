from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from models import User, db

bl_profile = Blueprint('profile', __name__, template_folder='templates')


@bl_profile.route('/profile')
def profile():
    template = 'profile/profile.html'
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(email=session['email']).first()
    if user:
        return render_template(template, user=user)
    else:
        flash('User not found')