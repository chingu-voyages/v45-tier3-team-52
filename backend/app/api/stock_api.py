from flask import Blueprint, jsonify, request, redirect
from app.models import Stock, db
import os
import urllib.request
import json

stock_route = Blueprint("stocks",  __name__)


@stock_route.route('/allstocks')
def list_of_stock():
    url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-08-25?adjusted=true&apiKey=3mbpuGf_xLfapcw7OPTqTf8_tFpGVDZk"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return jsonify(dict["results"])


@stock_route.route('/<int:id>')
def stock(id):
    stock = Stock.query.get_or_404(id)
    return stock.to_dict()
# print(stock_list)

# stock_routes = Blueprint("stocks", __name__)


# @stock_routes.route('/stocks', method=['Get'])
# def get_stocks():
#     url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-01-09?adjusted=true&apiKey={}".format(
#         os.environ.get("API_KEY"))

#     response = urllib.request.urlopen(url)
#     data = response.read()
#     # dict = json.loads(data)
#     return jsonify(data)
#     # return render_template("", stocks=dict["results"])
