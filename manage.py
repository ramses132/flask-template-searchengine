import os
import subprocess
import sys

from flask.cli import FlaskGroup
from flask_migrate import MigrateCommand
from flask_script import Command, Manager, Option

from search import app  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config_class = os.environ.get('APP_SETTINGS','config.Config')
# app = create_app(config_class)

class GunicornServer(Command):
    """Run the app withing Gunicorn"""

    def get_options(self):
        from gunicorn.config import make_settings

        settings = make_settings()
        options = []
        for setting, klass in settings.items():
            if klass.const is not None:
                options.append(Option(*klass.cli, const=klass.const, action=klass.action))
            elif klass.cli:
                options.append(Option(*klass.cli, action=klass.action))

        return options
    
    def run (self, *args, **kwargs):
        run_args = sys.argv[2:]
        run_args.append('--reload')
        run_args.append('flask:app')
        subprocess.Popen([os.path.join(os.path.dirname(sys.executable), 'gunicorn')] + run_args).wait()

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', GunicornServer)
if __name__ == "__main__":
    manager.run()
