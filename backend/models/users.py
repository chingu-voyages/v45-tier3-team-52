from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime(
        timezone=True), server_default=func.now())

    # TODO: pending assessment for config
    # updated_date = db.Column(db.DateTime(
    #     timezone=True), server_default=func.now())

    # ! Relationships
    owner_name = db.relationship(
        'user_portfolio', back_populates="name_owner", cascade="all, delete")
    owner_transactions = db.relationship(
        'transactions', back_populates="transactions_owner", cascade="all, delete")

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
            'userPortfolio': self.owner_name,
            'userTransactions': [transaction.to_dict() for transaction in self.owner_transactions]
        }

