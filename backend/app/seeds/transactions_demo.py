from app.models import db, Transaction, environment, SCHEMA
from sqlalchemy import text


def undo_transaction():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM transactions"))

    db.session.commit()
