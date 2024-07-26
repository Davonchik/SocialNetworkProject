from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import User, db, Post, Comment

bl_post = Blueprint('post', __name__, template_folder='templates')


@bl_post.route('/add_post', methods=['GET', 'POST'])
def add_post():
    template = 'post/add_post.html'
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(email=session['email']).first()
    if user:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            cur_post = Post(title=title, content=content, user_id=user.id)
            db.session.add(cur_post)
            db.session.commit()
        return render_template(template, user=user)
    else:
        flash('User not found')


@bl_post.route('/post', methods=['GET', 'POST'])
def post():
    template = 'post/post.html'
    post = Post.query.all()
    print(post[0].user.username)
    return render_template(template, post=post)


@bl_post.route('/post/<int:post_id>', methods=["GET", "POST"])
def add_comment(post_id):
    template = 'post/post_details.html'
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(email=session['email']).first()
    post = Post.query.filter_by(id=post_id).first()
    comment = Comment.query.filter_by(post_id=post_id).all()
    if user:
        if request.method == 'POST':
            text = request.form['comment']
            comment = Comment(user_id=user.id, post_id=post_id, text=text)
            db.session.add(comment)
            db.session.commit()
            print(text)
        return render_template(template, user=user, post=post, comment=comment)
    else:
        flash('User not found')

