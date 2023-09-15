from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import Transaction, Stock, db, UserPortfolio, User

transaction_routes = Blueprint("transaction", __name__)
auth_error = "User not authorized to complete this action"

##### * Get Transaction ###############


@transaction_routes.route('/<int:id>')
@login_required
def transaction(id):
    queried_transaction = Transaction.query.get_or_404(id)

    return queried_transaction.to_dict()


##### * Create Transaction ###############

@transaction_routes.route('/new', methods=['POST'])
@login_required
def transaction_creation():
    req_data = request.json

    # ? query for user portfolio
    queried_portfolio = UserPortfolio.query.filter(
        UserPortfolio.user_id == current_user.id).first()

    # * query for current logged in user
    queried_user = User.query.get_or_404(current_user.id)

    new_transaction = Transaction(
        user_id=current_user.id,
        portfolio_id=queried_portfolio.id,
        classification=req_data['type']
    )
    # Type: "Buy" /"Sell"
    db.session.add(new_transaction)
    db.session.commit()

    # query for the new transaction
    queried_transaction = Transaction.query.get_or_404(new_transaction.id)
    queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
    if req_data['stock'] and req_data['stock'] != None:
        queried_stock.quantity_stock = req_data['stock']['quantity']
        queried_transaction.transactions_stock.append(
            queried_stock)

        queried_transaction.total = float(
            req_data['stock']['quantity']) * float(queried_stock.current_price)
        db.session.commit()

    #! update the user portfolio and user wallet
    if req_data['type'] == 'Buy' and queried_stock.id not in queried_portfolio.to_dict()['stocks']:

        if queried_transaction.total <= queried_user.wallet:
            queried_user.wallet -= queried_transaction.total
            queried_portfolio.portfolio_stock.append(queried_stock)

    if req_data['type'] == 'Buy' and queried_stock.id in queried_portfolio.to_dict()['stocks']:
        if queried_transaction.total <= queried_user.wallet:
            queried_user.wallet -= queried_transaction.total
            queried_portfolio.find_stock(
                queried_stock.id, req_data['stock'])

    else:
        queried_user.wallet += queried_transaction.total
    db.session.commit()
    return queried_transaction.to_dict()
