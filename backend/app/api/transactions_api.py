from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import Transaction, db, User, StockTransactions

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
        status='In-progress',
    )

    db.session.add(new_transaction)
    db.session.commit()

    return new_transaction.to_dict()
