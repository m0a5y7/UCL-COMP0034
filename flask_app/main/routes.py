import requests
from flask import Blueprint, render_template, flash, g, redirect, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from flask_app.main.forms import ProfileForm, BlogForm
from flask_app.models import Profile, User, Blog
from flask_app import db, allowed_file, app
from datetime import datetime, timedelta
import os

main_bp = Blueprint('main', __name__)


@main_bp.route('/', defaults={'name': 'Anonymous'})
@main_bp.route('/<name>')
def index(name):
    if not current_user.is_anonymous:
        name = current_user.first_name
    api_key = 'da6f2470a88b4a74a2ff4163c97be84d'
    search = 'business'
    newest = datetime.today().strftime('%Y-%m-%d')
    oldest = (datetime.today() - timedelta(hours=1)).strftime('%Y-%m-%d')
    sort_by = 'publishedAt'
    url = f'https://newsapi.org/v2/everything?q={search}&from={oldest}&to={newest}&sortBy={sort_by}'

    response = requests.get(url, headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key)
    })
    news = response.json()
    return render_template('index.html', title='Home page', name=name, news=news)


@main_bp.route('/choropleth_app')
def choropleth_app():
    return redirect('/choropleth_app/')


@main_bp.route('/scatter_app')
def scatter_app():
    return redirect('/scatter_app/')


@main_bp.route('/line_app')
def line_app():
    return redirect('/line_app/')


@main_bp.route('/table_app')
def table_app():
    return redirect('/table_app/')


@main_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile = Profile.query.join(User, User.id == Profile.user_id).filter(User.id == current_user.id).first()
    if profile:
        return render_template('display_profile.html', username=profile.username, profile=profile, os=os)
    else:
        return redirect(url_for('main.create_profile'))


@main_bp.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():
    form = ProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        filename = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        p = Profile(username=form.username.data, photo=filename, bio=form.bio.data, user_id=current_user.id)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.profile', username=p.username))
    return render_template('profile.html', form=form)


@main_bp.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    profile = Profile.query.join(User, User.id == Profile.user_id).filter_by(id=current_user.id).first()
    form = ProfileForm(obj=profile)
    if request.method == 'POST' and form.validate_on_submit():
        filename = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        profile.photo = filename
        profile.bio = form.bio.data
        profile.username = form.username.data
        db.session.commit()
        return redirect(url_for('main.profile', username=profile.username))
    return render_template('profile.html', form=form)


@main_bp.route('/blog')
def blog():
    form = BlogForm()
    posts = Blog.query.all()
    return render_template('blog_index.html', user=current_user, posts=posts, form=form)


# Blog routes and html adapted from code written by user techwithtim on Github
# Link: https://github.com/techwithtim/Flask-Blog-Tutorial/blob/main/tutorial5/website/templates/create_post.html
@main_bp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogForm()
    if request.method == 'POST':
        body = request.form.get('body')
        if not body:
            flash('Post cannot be empty.', category='error')
        else:
            post = Blog(body=body, author=current_user.first_name, publish_date=datetime.today())
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('main.blog'))

    return render_template('blog_create.html', user=current_user, form=form)


@main_bp.route("/delete_post/<id>")
@login_required
def delete_post(id):
    post = Blog.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.first_name != post.author:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('main.blog'))
