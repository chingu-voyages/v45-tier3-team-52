from .db import db, environment, SCHEMA
from sqlalchemy.sql import func
from datetime import datetime
from .asset_transactions import AssetTransactions


class Transaction(db.Model):
    __tablename__ = 'transactions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    classification = db.Column(
        db.String(4))
    total = db.Column(db.Float, default=0.00)
    portfolio_id = db.Column(db.Integer, db.ForeignKey(
        'user_portfolios.id'), nullable=False)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,

    )
    # ! Relationships
    transactions_asset = db.relationship(
        'Asset', secondary=AssetTransactions, back_populates="asset_transactions")

    # ? Methods
    def to_dict(self):
        asset_dict = None
        if self.transactions_asset:
            asset_dict = self.transactions_asset[0].transaction_dict()
        return {
            'id': self.id,
            'userId': self.user_id,
            'portfolioId': self.portfolio_id,
            'type': self.classification,
            'total': self.total,
            'asset': asset_dict,
        }
