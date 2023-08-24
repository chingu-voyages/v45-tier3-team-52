from .db import db, environment, SCHEMA, add_prefix_for_prod


StockTransactions = db.Table(
    'stock_transactions',
    db.Model.metadata,
    db.Column('transactions', db.Integer, db.ForeignKey(
        add_prefix_for_prod('transactions.id')), primary_key=True, nullable=False),
    db.Column('stocks', db.Integer, db.ForeignKey(
        add_prefix_for_prod('stocks.id')), primary_key=True, nullable=False)
)
if environment == "production":
    StockTransactions.schema = SCHEMA
