from .db import db, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import func
from .portfolio_stock import PortfolioStocks
from .stock_transactions import StockTransactions


class Stock(db.Model):
    __tablename__ = 'stocks'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(255), nullable=False)
    symbol = db.Column(db.String(255), nullable=False, unique=True)
    current_price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        # nullable=False
    )

    # ! Relationships
    stock_portfolio = db.relationship(
        'UserPortfolio', secondary=PortfolioStocks, back_populates='portfolio_stock')
    stock_transactions = db.relationship(
        'Transaction', secondary=StockTransactions, back_populates='transactions_stock')

    # ? Methods
    def to_dict(self):
        return {
            'id': self.id,
            'org_name': self.org_name,
            'symbol': self.symbol,
            'current_price': self.current_price,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }
