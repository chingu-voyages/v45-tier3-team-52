from app import db
from app.models import SCHEMA, environment
from sqlalchemy.sql import text


def seed_portfolio_stocks():
    pass


def undo_portfolio_stocks():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.portfolio_assets RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM portfolio_assets"))

    db.session.commit()
