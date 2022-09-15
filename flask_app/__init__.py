from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_app.config import DevelopmentConfig

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)


def init_app(config_class_name):
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    csrf.init_app(app)
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    configure_uploads(app, photos)

    return app


# to prevent cyclical importing with routes.py
app = init_app(DevelopmentConfig)


def create_app(app):
    register_dash_apps(app)

    with app.app_context():
        from flask_app.models import User, Profile, Blog
        db.create_all()

    from flask_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app


def register_dash_apps(app):
    with app.app_context():
        from flask_app.dash_app.apps.choropleth_app import ChoroplethApp
        from flask_app.dash_app.apps.scatter_app import ScatterApp
        from flask_app.dash_app.apps.line_app import LineApp
        from flask_app.dash_app.apps.table_app import TableApp

        choropleth_app = ChoroplethApp(app)
        choropleth_app.setup()
        _protect_dash_views(choropleth_app.app)

        scatter_app = ScatterApp(app)
        scatter_app.setup()
        _protect_dash_views(scatter_app.app)

        line_app = LineApp(app)
        line_app.setup()
        _protect_dash_views(line_app.app)

        table_app = TableApp(app)
        table_app.setup()
        _protect_dash_views(table_app.app)


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']