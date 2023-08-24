from .db import db, environment, SCHEMA
from sqlalchemy.sql import func
from datetime import datetime
from .stock_transactions import StockTransactions

class Transaction(db.Model):
    __tablename__ = 'transactions'

    if environment == "production":
        __table_args__ = {'schema' : SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False) #pending, processed, etc
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    # ! Relationships
    transactions_stock = db.relationship('Stock', secondary=StockTransactions, back_populates="stock_transactions")

    # ? Methods
    def to_dict(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'stockid': self.stockid,
            'quantity': self.quantity,
            'totalPrice': self.totalPrice,
            'status': self.status,
            'stocks' : [stock.to_dict() for stock in self.transactions_stock]
        }