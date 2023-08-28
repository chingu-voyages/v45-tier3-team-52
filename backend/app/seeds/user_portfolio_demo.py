from app.models import db, UserPortfolio, environment, SCHEMA
from sqlalchemy import text


def seed_portfolio():
    portfolios = [{"name": "Saving_portfolio",
                   "balance": 1000.0, "user_id": 1}, {"name": "my_saving",
                                                      "balance": 1000.0, "user_id": 2}]

    db.session.add_all([UserPortfolio(**portfolio)for portfolio in portfolios])
    db.session.commit()


def undo_portfolio():
    if environment == 'production':
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_portfolios RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_portfolios"))

    db.session.commit()
