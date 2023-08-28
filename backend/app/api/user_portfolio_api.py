from flask import request, Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, UserPortfolio, PortfolioStocks, User


portfolio_routes = Blueprint("portfolio", __name__)
auth_error = "User not authorized to complete this action"


#### * Get Portfolio ############
@portfolio_routes.route('/<int:id>')
# @login_required
def portfolio(id):
    queried_portfolio = UserPortfolio.query.get_or_404(id)
    # if queried_portfolio.to_dict()['ownerId'] != current_user.id:
    #     return jsonify({"error": auth_error}), 403

    return queried_portfolio.to_dict()

#### * Delete Portfolio ###############


@portfolio_routes.route()
# @login_required
def portfolio_delete(id):
    queried_portfolio = UserPortfolio.query.get_or_404(id)
    # if queried_portfolio.to_dict()['ownerId'] != current_user.id:
    #     return jsonify({"error": auth_error}), 403
    # else:
    # db.session.delete(queried_portfolio)
    # db.session.commit()
    return {'message': 'Successfully deleted'}


@portfolio_routes.route()
# @login_required
def portfolio_create():
    pass


#### * update Portfolio ##############

@portfolio_routes.route()
# @login_required
def portfolio_update(id):
    queried_portfolio = UserPortfolio.query.get_or_404(id)
    queried_owner = User.query.get_or_404(
        queried_portfolio.to_dict()['ownerId'])

    req_data = request.json

    # if queried_portfolio.to_dict()['ownerId'] != current_user.id:
    #     return jsonify({"error": auth_error}), 403
    # else:
    # for key, val in req_data.items():
    #     if key != None:
    #         setattr(queried_portfolio, key, val)
    #     db.session.commit()
    return queried_portfolio
