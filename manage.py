from application import application, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand) # `python manage.py db ___` is the command sequence

if __name__ == '__main__':
  manager.run()

# PostgreSQL version: 11.5 (same in production)
# https://stackoverflow.com/questions/32798937/cant-migrate-or-upgrade-database-with-flask-migrate-alembic/32803927
# ^^ useful for deploying new migrations to production
