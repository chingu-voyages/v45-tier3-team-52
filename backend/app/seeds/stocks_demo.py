from app import db
from app.models import Stock, SCHEMA, environment
from sqlalchemy.sql import text
from app.api.stock_api import add_stocks


def seed_stocks():
    add_stocks()


def undo_stocks():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM stocks"))

    db.session.commit()
