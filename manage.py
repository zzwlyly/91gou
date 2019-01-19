from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from apps import create_app, config

app = create_app(config.ENVI_DEV_KEY)

manager = Manager(app=app)
manager.add_command('start', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
