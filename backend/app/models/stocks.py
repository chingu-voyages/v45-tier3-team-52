from .db import db, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import func


class Stock(db.Model):
    __tablename__ = 'stocks'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(255), nullable=False)
    symbol = db.Column(db.String(255), nullable=False, unique=True)
    current_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,

    )

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

    def transaction_dict(self):
        return {
            'id': self.id,
            'org_name': self.org_name,
            'symbol': self.symbol,
            'current_price': self.current_price,
        }
