from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from datetime import datetime
from .portfolio_assets import PortfolioAssets


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

    )

    # ! Relationships

    transactions = db.relationship(
        'Transaction', backref='portfolio', lazy=True)
    portfolio_owner = db.relationship(
        'User', back_populates='owner_portfolio')
    portfolio_asset = db.relationship(
        'Asset', secondary=PortfolioAssets, back_populates='asset_portfolio')

    # ? Methods
    def to_dict(self):
        user_assets = [asset.to_dict() for asset in self.portfolio_asset]
        asset_dict = {}

        for asset in user_assets:
            stock_id = asset['stock_id']
            if stock_id in asset_dict:
                asset_dict[stock_id]['quantity'] += asset['quantity']
            else:
                asset_dict[stock_id] = asset.copy()  # Use a copy of the asset

        for stock_id, asset_info in asset_dict.items():
            asset_info.pop('stock_id', None)
        return {
            'id': self.id,
            'name': self.name,
            'ownerId': self.user_id,
            'marketValue': self.market_value,
            'transactions': [transaction.to_dict() for transaction in self.transactions],
            'assets': asset_dict
        }
