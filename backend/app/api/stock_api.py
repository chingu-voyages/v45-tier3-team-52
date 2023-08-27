from flask import Blueprint, jsonify, request, redirect
from app.models import Stock, db

stock_route = Blueprint("stocks",  __name__)
# client = RESTClient(os.getenv('API_KEY'))

# stock_list = cast(
#     HTTPResponse,
#     client.get_tickers(
#         market='stocks',
#         limit=50,
#         all_pages=True
#     )
# )


@stock_route.route('/stocks')
def list_of_stock():
    return jsonify("Hello World")

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
