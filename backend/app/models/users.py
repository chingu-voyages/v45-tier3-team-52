from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    wallet = db.Column(db.Float(100), default=1000.0)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # ! Relationships
    owner_transactions = db.relationship(
        'Transaction', backref='owner', lazy=True,  cascade='all, delete')
    owner_portfolio = db.relationship(
        'UserPortfolio', back_populates='portfolio_owner', cascade='all, delete')

    # ? Methods
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name':  self.last_name,
            'userTransactions': [transaction.to_dict() for transaction in self.owner_transactions]
        }
