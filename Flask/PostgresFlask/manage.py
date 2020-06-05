from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, postgres

migrate = Migrate(app, postgres)
manager = Manager(app)

manager.add_command('postgres', MigrateCommand)


if __name__ == '__main__':
    manager.run()