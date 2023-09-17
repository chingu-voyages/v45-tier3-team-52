from app import db
from app.models import SCHEMA, environment
from sqlalchemy.sql import text


def undo_asset_transactions():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.asset_transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM asset_transactions"))

    db.session.commit()
