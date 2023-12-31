from flask.cli import AppGroup
from .users_demo import seed_users, undo_users
from .user_portfolio_demo import seed_portfolio, undo_portfolio
from .transactions_demo import undo_transaction
from .stocks_demo import seed_stocks, undo_stocks
from .asset_transactions_demo import undo_asset_transactions
from .portfolio_stocks_demo import undo_portfolio_stocks
from .asset_demo import undo_assets
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.portfolio_assets RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_portfolios RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.assets RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")

        db.session.commit()
    else:
        undo_users()
        undo_stocks()
        undo_assets()
        undo_portfolio()
        undo_transaction()
        undo_asset_transactions()
        undo_portfolio_stocks()

    seed_users()
    seed_stocks()
    seed_portfolio()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_stocks()
    undo_assets()
    undo_portfolio()
    undo_transaction()
    undo_asset_transactions()
    undo_portfolio_stocks()
