from flask import request, Blueprint
from flask_login import login_required, current_user
from app.models import db, UserPortfolio, Stock


portfolio_routes = Blueprint("portfolio", __name__)
auth_error = "User not authorized to complete this action"


#### * update Portfolio ##############

@portfolio_routes.route('/<int:id>', methods=['PUT'])
@login_required
def portfolio_update(id):
    queried_portfolio = UserPortfolio.query.get_or_404(id)

    req_data = request.json

    if queried_portfolio.to_dict()['ownerId'] != current_user.id:
        return {"error": auth_error}, 403
    else:
        for key, val in req_data.items():
            if key == 'name':
                setattr(queried_portfolio, key, val)
            if key == 'stock' and val != None:
                queried_stock = Stock.query.get_or_404(req_data['stock']['id'])
                queried_portfolio.portfolio_stock.append(
                    queried_stock)
                stock_count = req_data['stock']['quantity']
                stock_price = queried_stock.current_price

            db.session.commit()
    return queried_portfolio.to_dict()


# queried_transaction.total = int(stock_count) * int(stock_price)
