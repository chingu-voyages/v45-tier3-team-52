from app import db
from app.models import stock_transactions, SCHEMA, environment
from sqlalchemy.sql import text


def seed_stock_transactions():
    pass


def undo_stock_transactions():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stock_transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM stock_transactions"))

    db.session.commit()
