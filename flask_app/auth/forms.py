from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo
from flask_app.auth.validators import NewEmail, ValidPassword, ValidateEmail, ValidatePassword


class SignupForm(FlaskForm):
    # add pw limit
    first_name = StringField(label='First name', validators=[DataRequired(message='First name required')])
    last_name = StringField(label='Last name', validators=[DataRequired(message='Last name required')])
    email = EmailField(label='Email address', validators=[DataRequired(message='Email address required'), NewEmail])
    # pw must be a combination of letters, numbers, capital letters and special characters
    password = PasswordField(label='Password', render_kw={'placeholder': 'One uppercase letter, One special character, '
                                                                        'Two digits, Needs to be 4 or more characters '
                                                                        'long.'},
                             validators=[DataRequired(message='Password required'), ValidPassword])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])


class LoginForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired(), ValidateEmail])
    password = PasswordField(label='Password', validators=[DataRequired(), ValidatePassword])
    remember = BooleanField(label='Remember me')
