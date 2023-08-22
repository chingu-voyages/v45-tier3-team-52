from .db import db, environment, SCHEMA, add_prefix_for_prod



portfolio_stocks=db.Table(
    'portfolio_stocks',
    db.Model.metadata,
    db.column('portfolios', db.Integer, db.ForeignKey(add_prefix_for_prod('portfolios.id'))),
    db.column('stocks', db.Integer, db.ForeignKey(add_prefix_for_prod('stocks.id')))
)
if environment == "production":
    portfolio_stocks.schema = SCHEMA