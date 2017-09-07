from flask import Flask
from config import config

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    # register our blueprints
    from routes.main import main
    app.register_blueprint(main)  # regist URL

    from routes.user import user
    app.register_blueprint(user)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
