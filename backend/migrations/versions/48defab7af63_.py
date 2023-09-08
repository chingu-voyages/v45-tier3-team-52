"""empty message

<<<<<<<< HEAD:backend/migrations/versions/5f2ffceb2732_.py
Revision ID: 5f2ffceb2732
Revises: 
Create Date: 2023-09-05 17:27:33.345285
========
Revision ID: 48defab7af63
Revises: 
Create Date: 2023-09-02 13:50:44.538920
>>>>>>>> dev:backend/migrations/versions/48defab7af63_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:backend/migrations/versions/5f2ffceb2732_.py
revision = '5f2ffceb2732'
========
revision = '48defab7af63'
>>>>>>>> dev:backend/migrations/versions/48defab7af63_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('org_name', sa.String(length=255), nullable=False),
    sa.Column('symbol', sa.String(length=255), nullable=False),
    sa.Column('current_price', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('symbol')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('wallet', sa.Float(precision=100), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_portfolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio_stocks',
    sa.Column('user_portfolios', sa.Integer(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stocks'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['user_portfolios'], ['user_portfolios.id'], ),
    sa.PrimaryKeyConstraint('user_portfolios', 'stocks')
    )
    op.create_table('stock_transactions',
    sa.Column('transactions', sa.Integer(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stocks'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['transactions'], ['transactions.id'], ),
    sa.PrimaryKeyConstraint('transactions', 'stocks')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_transactions')
    op.drop_table('portfolio_stocks')
    op.drop_table('user_portfolios')
    op.drop_table('transactions')
    op.drop_table('users')
    op.drop_table('stocks')
    # ### end Alembic commands ###
