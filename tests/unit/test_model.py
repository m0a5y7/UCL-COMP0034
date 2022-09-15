from flask_app.models import User, Profile


def test_new_user_details_correct():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the first_name, last_name, email, and password fields are defined correctly
    """
    user_data = {
        'first_name': 'User',
        'last_name': 'Name',
        'password': 'asdf1234',
        'email': 'username@email.com'
    }

    user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'],
                password=user_data['password'])

    assert user.first_name == 'User'
    assert user.last_name == 'Name'
    assert user.email == 'username@email.com'
    assert user.password == 'asdf1234'


def test_profile_created():
    """
    GIVEN a Profile model
    WHEN a new Profile is created
    THEN check the username, bio, and photo fields are defined correctly
    """
    profile_data = {
        'username': 'user123',
        'bio': 'Hello there!',
        'photo': None
    }

    profile = Profile(username=profile_data['username'], photo=profile_data['photo'], bio=profile_data['bio'])

    assert profile.username == 'user123'
    assert profile.photo is None
    assert profile.bio == 'Hello there!'

