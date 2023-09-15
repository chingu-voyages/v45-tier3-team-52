from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from datetime import datetime
from .portfolio_stock import PortfolioStocks


class UserPortfolio(db.Model):
    """
    The UserPortfolio has one portfolio per user. Each portfolio can have multiple stocks.
    """
    __tablename__ = 'user_portfolios'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False,
                     default='Portfolio')
    market_value = db.Column(db.Float, default=0.00)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)

    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # ! Relationships

    transactions = db.relationship(
        'Transaction', backref='portfolio', lazy=True)
    portfolio_owner = db.relationship(
        'User', back_populates='owner_portfolio')
    portfolio_stock = db.relationship(
        'Stock', secondary=PortfolioStocks, back_populates='stock_portfolio')

    # ? Methods

#
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ownerId': self.user_id,
            'marketValue': self.market_value,
            'transactions': [transaction.to_dict() for transaction in self.transactions],
            'stocks': {stock.id: stock.transaction_dict() for stock in self.portfolio_stock}
        }

    def find_stock(self, stock_id):
        stocks = {stock.id: stock.transaction_dict()
                  for stock in self.portfolio_stock}
        if stock_id in stocks:
            return stocks[stock_id]
