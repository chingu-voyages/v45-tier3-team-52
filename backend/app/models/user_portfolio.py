from .db import db, environment, SCHEMA
from sqlalchemy.sql import func
from datetime import datetime
from .portfolio_stock import portfolio_stocks


class UserPortfolio(db.Model):
    """
    The UserPortfolio has one portfolio per user. Each portfolio can have multiple stocks.
    """
    __tablename__ = 'user_portfolios'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)  # what does name mean?
    balance = db.Column(db.Float(15))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    quantity_per_stock = db.Column(db.Integer)
    stock_num = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # stockId may need to be a relationship instead because it is many to many

    # ! Relationships
    portfolio_owner = db.relationship(
        'users', back_populates='owner_portfolio')
    portfolio_stock = db.relationship(
        'stocks', secondary=portfolio_stocks, back_populates='stock_portfolio')

    # ? Methods

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance,
            'quantityPerStock': self.quantity_per_stock,
            'stockTotal': self.stock_num,
        }
