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
    name = db.Column(db.String(255), nullable=False)
    symbol = db.Column(db.String(255), nullable=False, unique=True)
    abv = db.Column(db.String(255))
    currentPrice = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
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
            'name': self.name,
            'symbol': self.symbol,
            'abv': self.abv,
            'currentPrice': self.currentPrice,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'portfolio': [portfolio.to_dict() for portfolio in self.stock_portfolio]
        }
