from .db import db

class UserPortfolio(db.Model):
    """
    The UserPortfolio has one portfolio per user. Each portfolio can have multiple stocks. 
    """
    __tablename__ = 'user_portfolio'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64)) # what does name mean?
    balance = db.Column(db.Float(15))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    stockId = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable = False)
    quantityPerStock = db.Column(db.Integer)
    stockNum = db.Column(db.Integer)
    createdAt = db.Column(db.Date)
    updatedAt = db.Column(db.Date)
   
    # stockId may need to be a relationship instead because it is many to many 

