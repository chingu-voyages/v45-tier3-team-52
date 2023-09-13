from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import Transaction, Stock, db, UserPortfolio

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

    # queried_portfolio = UserPortfolio.query.filter(UserPortfolio
    #     current_user.portfolio.id)

    new_transaction = Transaction(
        user_id=current_user.id,
        portfolio_id=queried_portfolio.id,
        classification=req_data['type']
    )

    db.session.add(new_transaction)
    db.session.commit()

    queried_transaction = Transaction.query.get_or_404(new_transaction.id)

    for key, val in req_data.items():
        if key == 'stock' and val != None:
            queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
            queried_stock.quantity_stock = req_data['stock']['quantity']
            queried_transaction.transactions_stock.append(
                queried_stock)

            queried_transaction.total = float(
                req_data['stock']['quantity']) * float(queried_stock.current_price)
            queried_transaction.quantity = req_data['stock']['quantity']

            queried_portfolio = UserPortfolio.query.get_or_404(
                new_transaction.portfolio_id)

            if queried_stock in queried_portfolio.portfolio_stock:
                pass
            else:
                queried_portfolio.portfolio_stock.append(queried_stock)
                if key == 'type' and val == 'Buy':
                    print('key====>', key, val)
                    queried_portfolio.market_value = queried_portfolio.market_value + \
                        queried_transaction.total
                if key == 'type' and val == 'Sell':
                    queried_portfolio.market_value = queried_portfolio.market_value - \
                        queried_transaction.total
        if key == 'stock' and val == None:
            return {"message": "you need to provide a stock"}
        db.session.commit()
    return queried_transaction.to_dict()
