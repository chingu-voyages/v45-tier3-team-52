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
    queried_portfolio = UserPortfolio.query.filter(
        UserPortfolio.user_id == current_user.id).first()
    queried_user = User.query.get_or_404(current_user.id)

    new_transaction = Transaction(
        user_id=current_user.id,
        portfolio_id=queried_portfolio.id,
        classification=req_data['type']
    )
    # Type: "Buy" /"Sell"
    db.session.add(new_transaction)
    db.session.commit()

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
    if req_data['type'] == 'Buy':
        print("test ========>", queried_portfolio.to_dict()['stocks'])
        if queried_transaction.total <= queried_user.wallet:
            queried_user.wallet -= queried_transaction.total
            queried_portfolio.portfolio_stock.append(queried_stock)
        else:
            if queried_transaction.total <= queried_user.wallet:
                queried_user.wallet -= queried_transaction.total
                print('queried_portfolio.portfolio_stock ====>',
                      queried_portfolio.portfolio_stock)
    else:
        queried_user.wallet += queried_transaction.total
    db.session.commit()
    return queried_transaction.to_dict()


# for key, val in req_data.items():
#         if key == 'stock' and val != None:
#             queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
#             # stock : {quantity: 2, id: 2}
#             queried_stock.quantity_stock = req_data['stock']['quantity']
#             queried_transaction.transactions_stock.append(
#                 queried_stock)

#             queried_transaction.total = float(
#                 req_data['stock']['quantity']) * float(queried_stock.current_price)

#             if req_data['type'] == 'Buy':
#                 if queried_transaction.total <= queried_user.wallet:
#                     queried_user.wallet -= queried_transaction.total
#                 else:
#                     return {"error": "Not enough funds to make this transaction!"}
#             else:
#                 queried_user.wallet += queried_transaction.total
#             db.session.commit()
#         if key == 'type' and val == 'Buy':
#             pass
#         else:
#             return {"message": "you need to provide a stock"}
#         # db.session.commit()
#     return queried_transaction.to_dict()
