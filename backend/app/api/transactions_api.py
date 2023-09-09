from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import Transaction, Stock, db, User, StockTransactions

transaction_routes = Blueprint("transaction", __name__)
auth_error = "User not authorized to complete this action"

##### * Get Transaction ###############


@transaction_routes.route('/<int:id>')
# @login_required
def transaction(id):
    queried_transaction = Transaction.query.get_or_404(id)

    return queried_transaction.to_dict()


##### * Create Transaction ###############

@transaction_routes.route('/new', methods=['POST'])
# @login_required
def transaction_creation():
    req_data = request.json

    new_transaction = Transaction(
        user_id=req_data['userId'],
        # user_id=current_user.id,
        status='In-Progress',
    )

    db.session.add(new_transaction)
    db.session.commit()

    queried_transaction = Transaction.query.get_or_404(new_transaction.id)

    for key, val in req_data.items():
        if key == 'stock' and val != None:
            queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
            queried_transaction.transactions_stock.append(
                queried_stock)
            stock_count = req_data['stock']['quantity']
            stock_price = queried_stock.current_price
            queried_transaction.total = int(stock_count) * int(stock_price)
            queried_transaction.status = 'completed'
            db.session.commit()
        if key == 'stock' and val == None:
            return {"message": "you need to provide a stock"}
    return queried_transaction.to_dict()
