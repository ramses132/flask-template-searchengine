import os

from flask import Flask

from dotenv import load_dotenv
from pathlib import Path


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev'
            DATABASE=os.path.join(app.instance_path, 'search.sqlite',)
            )
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        osmakedirs(app.instance_path)
    except OSError:
        pass
    
    #a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

