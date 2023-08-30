from app.models import db, Transaction, environment, SCHEMA
from sqlalchemy import text


def seed_transaction():
    transactions = [{"user_id": 1, "status": "completed"}, {"user_id": 2, "status": "completed"}, {"user_id": 3, "status": "completed"}, {"user_id": 4, "status": "completed"}, {
        "user_id": 5, "status": "completed"}, {"user_id": 6, "status": "completed"}, {"user_id": 7, "status": "completed"}, {"user_id": 8, "status": "completed"},]
    db.session.add_all([Transaction(**transaction)
                       for transaction in transactions])
    db.session.commit()


def undo_transaction():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM transactions"))

    db.session.commit()
