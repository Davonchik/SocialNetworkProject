from flask import Blueprint, render_template, session, redirect, url_for

bl_profile = Blueprint('profile', __name__, template_folder='templates')


@bl_profile.route('/profile')
def profile():
    template = 'profile/profile.html'
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    print(session['email'])
    return render_template(template)