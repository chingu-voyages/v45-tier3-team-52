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
# @login_required
def transaction_creation():
    req_data = request.json

    portfolio_num = current_user.to_dict()['portfolio']['id']
    new_transaction = Transaction(
        user_id=current_user.id,
        portfolio_id=portfolio_num
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
            queried_transaction.status = 'completed'
            queried_transaction.quantity = req_data['stock']['quantity']

            queried_portfolio = UserPortfolio.query.get_or_404(
                new_transaction.portfolio_id)

            if queried_stock in queried_portfolio.portfolio_stock:
                pass
            else:
                queried_portfolio.portfolio_stock.append(queried_stock)
            db.session.commit()
        if key == 'stock' and val == None:
            return {"message": "you need to provide a stock"}
    return queried_transaction.to_dict()


# # Assuming you have already queried the stock and portfolio as shown in your question

# # Check if the queried_stock is already in the portfolio's portfolio_stock list
# if queried_stock in queried_portfolio.portfolio_stock:
#     # The stock is already in the portfolio
#     # You can handle this case here
#     pass
# else:
#     # The stock is not in the portfolio, so you can add it
#     queried_portfolio.portfolio_stock.append(queried_stock)

#     # Now you can perform the rest of your operations
#     queried_transaction.total = float(req_data['stock']['quantity']) * float(queried_stock.current_price)
#     queried_transaction.status = 'completed'
#     queried_transaction.quantity = req_data['stock']['quantity']

#     db.session.commit()
