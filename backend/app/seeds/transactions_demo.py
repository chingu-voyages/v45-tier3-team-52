from app.models import db, Transaction, environment, SCHEMA
from sqlalchemy import text


def seed_transaction():
    transactions = [{"user_id": 1, "status": "completed", "portfolio_id": 1}, {"user_id": 2, "status": "completed", "portfolio_id": 2}, {"user_id": 3, "status": "completed", "portfolio_id": 3}, {"user_id": 4, "status": "completed", "portfolio_id": 4}, {
        "user_id": 5, "status": "completed", "portfolio_id": 5}, {"user_id": 6, "status": "completed", "portfolio_id": 6}, {"user_id": 7, "status": "completed", "portfolio_id": 7}, {"user_id": 8, "status": "completed", "portfolio_id": 8}, {"user_id": 9, "status": "completed", "portfolio_id": 9}, {"user_id": 10, "status": "completed", "portfolio_id": 10}, {"user_id": 11, "status": "completed", "portfolio_id": 11}, {"user_id": 12, "status": "completed", "portfolio_id": 12}, {"user_id": 13, "status": "completed", "portfolio_id": 13}, {"user_id": 14, "status": "completed", "portfolio_id": 14}, {"user_id": 15, "status": "completed", "portfolio_id": 15}]
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
