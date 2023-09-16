from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Asset

asset_routes = Blueprint("assets", __name__)


####### * Get Asset ##############################

@asset_routes.route('/')
@login_required
def assets():
    assets = Asset.query.filter(Asset.user_id == current_user.id).all()

    asset_dict = {}
    for asset in assets:
        stock_id = asset.stock_id
        if stock_id in asset_dict:
            asset_dict[stock_id]['quantity'] += asset.quantity
        else:
            asset_dict[stock_id] = asset.to_dict()
    return asset_dict
