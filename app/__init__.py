from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
#
from config import config

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
    # customize app.config
    # app.config['option']= "option"

    bootstrap.init_app(app)

    # register our blueprints

    from user.views import user_app
    app.register_blueprint(user_app)

    return app
