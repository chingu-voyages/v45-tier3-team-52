from .db import db, environment, SCHEMA
from sqlalchemy.sql import func

class Transaction(db.Model):
    __tablename__ = 'transactions'

    if environment == "production":
        __table_args__ = {'schema' : SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey(db.add_prefix_for_prod('user.id')), nullable=False)
    stockid = db.Column(db.Integer, db.ForeignKey(db.add_prefix_for_prod('stock.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False) #pending, processed, etc
    totalPrice = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    
    # ! Relationships
    transactions_owner = db.relationship('users', back_populates="owner_transactions")
    # stocks_owner = db.relationship('stocks', back_populates="owner_stocks")
    
    def to_dict(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'stockid': self.stockid,
            'quantity': self.quantity,
            'totalPrice': self.totalPrice,
            'status': self.status,
            'transaction_owner': {
                'id': self.transactions_owner.id,
                'first_name': self.transactions_owner.first_name,
                'last_name':  self.transactions_owner.last_name,
                'userPortfolio': self.transactions_owner.owner_name,
              }
        }