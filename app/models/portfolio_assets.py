from .db import db, environment, SCHEMA, add_prefix_for_prod

PortfolioAssets = db.Table(
    'portfolio_assets',
    db.Model.metadata,
    db.Column('user_portfolios', db.Integer, db.ForeignKey(
        add_prefix_for_prod('user_portfolios.id')), primary_key=True, nullable=False),
    db.Column('stocks', db.Integer, db.ForeignKey(
        add_prefix_for_prod('assets.id')), primary_key=True, nullable=False)
)
if environment == "production":
    PortfolioAssets.schema = SCHEMA
