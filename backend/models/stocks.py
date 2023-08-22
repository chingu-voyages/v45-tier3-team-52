from .db import db, environment, SCHEMA
from datetime import datetime
from .portfolio_stock import portfolio_stocks

class Stock(db.Model):
    __tablename__='stocks'
    if environment == "production":
        __table_args__ = {'schema' : SCHEMA}
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    symbol=db.Column(db.String(255), nullable=False, unique=True)
    abv=db.Column(db.String(255))
    currentPrice=db.Column(db.Integer)

    portfolios=db.relationship('Portfolio', secondary=portfolio_stocks,back_populates='stocks')
   
    createdAt = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updatedAt = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'symbol':self.symbol,
            'abv':self.abv,
            'currentPrice':self.currentPrice,
            'createdAt':self.createdAt,
            'updatedAt':self.updatedAt,
            'portfolios':self.portfolios.to_dict()

        }
