from flask import Blueprint, jsonify, request, redirect
from app.models import Stock, db
import os
import urllib.request
import json
import yfinance as yf
from sqlalchemy import func, or_

stock_route = Blueprint("stocks",  __name__)

polygon_API = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-08-25?adjusted=true&sort=desc&apiKey={}".format(
    os.getenv('API_KEY'))


def api_data(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict['results']


def ticker_list(stocks):
    newlist = []
    count = 0
    while count <= 100:
        newlist.append(
            {"ticker_name": stocks[count]["T"], "close_price": stocks[count]['c']})
        count += 1
    return newlist


def convert_symbol_to_company(ticker_list):
    stock_list = []
    for ticker_info in ticker_list:
        ticker_name = ticker_info['ticker_name']
        try:
            ticker = yf.Ticker(ticker_name)
            long_name = ticker.info.get('longName', None)
            if long_name:
                stock_list.append({
                    'symbol': ticker_name,
                    'org_name': long_name,
                    'current_price': ticker_info['close_price']
                })
        except Exception as e:
            print(f"Error fetching data for {ticker_name}: {str(e)}")
    return stock_list


@stock_route.route('/allstocks')
def list_of_stock():
    return api_data(polygon_API)


@stock_route.route('/<value>', methods=['GET'])
def get_stock(value):
    """
    Route allowing user to query stock by id, symbol, or orgname.
    """
    stock = None

    # Try querying by ID
    if value.isdigit():
        stock = Stock.query.get(int(value))

    # If not found by ID, try querying by symbol (case-insensitive)
    if stock is None:
        stock = Stock.query.filter(or_(
            func.lower(Stock.symbol) == value.lower(),
            func.lower(Stock.org_name) == value.lower()
        )).first()
    if stock is None:
        return jsonify({'error': 'Stock not found'}), 404

    return stock.to_dict()


@stock_route.route('/addstock', methods=["POST"])
def add_stocks():
    db_stocks = []
    aggs = convert_symbol_to_company(ticker_list(api_data(polygon_API)))
    for stock_currated in aggs:
        new_stock = Stock(
            org_name=stock_currated['org_name'],
            symbol=stock_currated['symbol'],
            current_price=stock_currated['current_price']
        )
        db_stocks.append(new_stock)
    db.session.add_all(db_stocks)
    db.session.commit()
    return [stock_db.to_dict() for stock_db in db_stocks], {'message': "Sucess 200"}
