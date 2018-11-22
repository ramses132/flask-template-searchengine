import os

from flask import Flask
from pathlib import Path
from config import config


def create_app(config_name):
    # create and configure the app
    print(config_class)
    app = Flask(__name__, instance_relative_config=True)

    # load the instance config, if it exists, when not testing
    app.config.from_object(config[config_name])
    config[config_name].init_app(ap)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
