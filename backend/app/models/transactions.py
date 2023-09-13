from .db import db, environment, SCHEMA
from sqlalchemy.sql import func
from datetime import datetime
from .stock_transactions import StockTransactions


class Transaction(db.Model):
    __tablename__ = 'transactions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    classification = db.Column(
        db.String(4))
    quantity = db.Column(db.Integer, default=0)
    total = db.Column(db.Float, default=0.00)
    portfolio_id = db.Column(db.Integer, db.ForeignKey(
        'user_portfolios.id'), nullable=False)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    # ! Relationships
    transactions_stock = db.relationship(
        'Stock', secondary=StockTransactions, back_populates="stock_transactions")

    # ? Methods
    def to_dict(self):
        stock_dict = None
        if self.transactions_stock:
            stock_dict = self.transactions_stock[0].transaction_dict()
        return {
            'id': self.id,
            'userId': self.user_id,
            'portfolioId': self.portfolio_id,
            'type': self.classification,
            'quantity': self.quantity,
            'total': self.total,
            'stock': stock_dict,
        }
