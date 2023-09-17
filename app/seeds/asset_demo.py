from app import db
from app.models import Asset, SCHEMA, environment
from sqlalchemy.sql import text


def undo_assets():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM assets"))

    db.session.commit()
