from .db import db, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import func
from .portfolio_assets import PortfolioAssets
from .asset_transactions import AssetTransactions


class Asset(db.Model):
    __tablename__ = 'assets'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(255), nullable=False)
    symbol = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    stock_id = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Float)
    quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,

    )

    # ! Relationships
    asset_portfolio = db.relationship(
        'UserPortfolio', secondary=PortfolioAssets, back_populates='portfolio_asset')
    asset_transactions = db.relationship(
        'Transaction', secondary=AssetTransactions, back_populates='transactions_asset')

    # ? Methods
    def to_dict(self):
        return {
            'id': self.id,
            'org_name': self.org_name,
            'symbol': self.symbol,
            'stock_id': self.stock_id,
            'quantity': self.quantity,
            'current_price': self.current_price,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }

    def transaction_dict(self):
        return {
            'id': self.id,
            'org_name': self.org_name,
            'stock_id': self.stock_id,
            'symbol': self.symbol,
            'current_price': self.current_price,
            'quantity': self.quantity
        }
