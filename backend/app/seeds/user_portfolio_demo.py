from app.models import db, UserPortfolio, environment, SCHEMA
from sqlalchemy import text


def seed_portfolio():
    portfolios = [{"name": "Saving_portfolio",
                   "user_id": 1}, {"name": "my_saving",
                                   "user_id": 2}, {"name": "my_savings",
                                                   "user_id": 3}, {"name": "my_stocks",
                                                                   "user_id": 4}, {"name": "Money",
                                                                                   "user_id": 5}, {"name": "longTerm",
                                                                                                   "user_id": 6}, {"name": "Savings",
                                                                                                                   "user_id": 7}, {"name": "wallet",
                                                                                                                                   "user_id": 8}]

    db.session.add_all([UserPortfolio(**portfolio)for portfolio in portfolios])
    db.session.commit()


def undo_portfolio():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_portfolios RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_portfolios"))

    db.session.commit()
