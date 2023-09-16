from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import Transaction, Asset, Stock, db, UserPortfolio, User

transaction_routes = Blueprint("transaction", __name__)
auth_error = "User not authorized to complete this action"


##### * Get Transaction ###############


@transaction_routes.route('/<int:id>')
@login_required
def transaction(id):
    queried_transaction = Transaction.query.get_or_404(id)

    return queried_transaction.to_dict()


##### * Create Purchase Transaction ###############

@transaction_routes.route('/buy', methods=['POST'])
@login_required
def transaction_buy():
    req_data = request.json

    queried_portfolio = UserPortfolio.query.filter(
        UserPortfolio.user_id == current_user.id).first()
    queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
    transaction_total = float(
        req_data['stock']['quantity']) * float(queried_stock.current_price)

    # * Type: "Buy"
    if req_data['type'] == 'Buy' and current_user.wallet >= transaction_total:

        new_transaction = Transaction(
            user_id=current_user.id,
            classification=req_data['type'],
            portfolio_id=queried_portfolio.id,
            total=transaction_total
        )

        db.session.add(new_transaction)
        db.session.commit()

        # * query for the new transaction
        queried_transaction = Transaction.query.get_or_404(new_transaction.id)

        new_asset = Asset(
            org_name=queried_stock.org_name,
            symbol=queried_stock.symbol,
            user_id=current_user.id,
            stock_id=queried_stock.id,
            current_price=queried_stock.current_price,
            quantity=req_data['stock']['quantity']
        )
        queried_transaction.transactions_asset.append(
            new_asset)
        queried_portfolio.portfolio_asset.append(new_asset)
        # * update user wallet
        current_user.wallet -= new_transaction.total
        queried_portfolio.market_value += new_transaction.total
    else:
        return {'error': "Insufficient funds"}
    db.session.commit()
    return queried_transaction.to_dict()


##### * Create Sell Transaction ###############

# @transaction_routes.route('/sell', methods=['PUT'])
# @login_required
# def transaction_sell():
#     req_data = request.json

#     queried_portfolio = UserPortfolio.query.filter(
#         UserPortfolio.user_id == current_user.id).first()

#     queried_stock = Stock.query.get_or_404(req_data['stock']['id'])

#     transaction_total = float(
#         req_data['stock']['quantity']) * float(queried_stock.current_price)

#     # * Type: "Sell"
#     if req_data['type'] == 'Sell':

#         new_transaction = Transaction(
#             user_id=current_user.id,
#             classification=req_data['type'],
#             portfolio_id=queried_portfolio.id,
#             total=transaction_total
#         )

#         db.session.add(new_transaction)
#         db.session.commit()

#         # * query for the new transaction
#         queried_transaction = Transaction.query.get_or_404(new_transaction.id)

#         assets = Asset.query.filter(
#             Asset.user_id == current_user.id and Asset.stock_id == queried_stock['stock']['id']).all()

#         quantity_to_delete = int(req_data['stock']['quantity'])
#         if assets != None and quantity_to_delete <= len(assets):
#             queried_asset = Asset.query.filter(
#                 Asset.user_id == current_user.id and Asset.stock_id == queried_stock['stock']['id']).first()
#             queried_transaction.transactions_asset.append(
#                 queried_asset)

#             for _ in range(quantity_to_delete):
#                 asset = assets.pop(0)
#                 db.session.delete(asset)
#         # * update user wallet
#         current_user.wallet += new_transaction.total
#     db.session.commit()
#     return queried_transaction.to_dict()
