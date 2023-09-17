from .db import db, environment, SCHEMA, add_prefix_for_prod

AssetTransactions = db.Table(
    'asset_transactions',
    db.Model.metadata,
    db.Column('transactions', db.Integer, db.ForeignKey(
        add_prefix_for_prod('transactions.id')), primary_key=True, nullable=False),
    db.Column('assets', db.Integer, db.ForeignKey(
        add_prefix_for_prod('assets.id')), primary_key=True, nullable=False)
)
if environment == "production":
    AssetTransactions.schema = SCHEMA
