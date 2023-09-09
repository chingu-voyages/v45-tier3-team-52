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
    status = db.Column(db.String(255), nullable=False, default="In-progress")
    total = db.Column(db.Integer, default=0)
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
        return {
            'id': self.id,
            'userId': self.user_id,
            'status': self.status,
            'stocks': [stock.to_dict() for stock in self.transactions_stock],
            'total': self.total,
        }
