import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    # create and configure the app

    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    db.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)
    

    #a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
