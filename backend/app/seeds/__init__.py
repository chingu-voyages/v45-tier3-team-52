from flask.cli import AppGroup
from .users_demo import seed_users, undo_users
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")

        db.session.commit()
    else:
        undo_users()

    seed_users()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
