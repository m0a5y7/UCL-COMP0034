import re
from flask_app.models import User
from wtforms.validators import ValidationError


def NewEmail(form, field):
    users = User.query.filter_by(email=field.data).first()
    if users is not None:
        raise ValidationError('An account is already registered for that email address')

'''
Password rules:
(?=.*[A-Z])               Ensure string has оne uppercase letter.
(?=.*[!@#$&*])            Ensure string has one special case letter.
(?=.*[0-9].*[0-9])        Ensure string has two digits.
.{4,}                     Ensure string is of length 4 or more.
'''


def ValidPassword(form, field):
    if not re.search(r'(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9]).{4,}', field.data):
        raise ValidationError('''Password rules: One uppercase letter, One special character,  
                            Two digits, Needs to be 4 or more characters long. ''')


def ValidateEmail(form, field):
    user = User.query.filter_by(email=field.data).first()
    if user is None:
        raise ValidationError('No account found with that email address.')


def ValidatePassword(form, field):
    user = User.query.filter_by(email=form.email.data).first()
    if user is None:
        raise ValidationError('No account found with that email address.')
    if not user.check_password(field.data):
        raise ValidationError('Incorrect password.')