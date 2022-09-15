import pytest
from flask_app import init_app, config, create_app
from flask_app import db as _db
from flask_app.models import User


@pytest.fixture(scope='session')
def app():
    """Create a Flask app for the testing"""
    app = init_app(config_class_name=config.TestingConfig)
    app = create_app(app)
    yield app


@pytest.fixture(scope='session')
def test_client(app):
    """Create a Flask test client using the Flask app."""
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def user_data():
    """ Data to create a new user"""
    user_data = {
        'first_name': 'User',
        'last_name': 'Name',
        'password': 'ASDf123!',
        'email': 'asdf@user.com'
    }
    yield user_data


@pytest.fixture(scope='module')
def new_user(user_data):
    """ Create a user without a profile and add them to the database. Allow the user object to be used in tests. """
    user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'],
                password=user_data['password'])
    yield user


@pytest.fixture(scope='session')
def db(app):
    """
    Return a session wide database using a Flask-SQLAlchemy database connection.
    """
    with app.app_context():
        _db.app = app
        _db.create_all()
    yield _db
    _db.drop_all()