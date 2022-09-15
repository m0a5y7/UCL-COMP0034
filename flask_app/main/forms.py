from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

from flask_app import photos
from flask_app.models import Profile


class ProfileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='Username is required')])
    bio = TextAreaField(label='Bio', description='Tell us about yourself!')
    photo = FileField('Profile picture', validators=[FileAllowed(photos, 'Images only!')])

    def validate_username(self, username):
        profile = Profile.query.filter_by(username=username.data).first()
        if profile is not None:
            raise ValidationError('Username already exists, please choose another username')


class BlogForm(FlaskForm):
    post = TextAreaField(label='Post', description='What is on your mind?')
