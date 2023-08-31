from flask import Blueprint, jsonify, request, redirect
from app.models import Stock, db
import os
import urllib.request
import json
import yfinance as yf

stock_route = Blueprint("stocks",  __name__)

polygon_API = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-08-25?adjusted=true&apiKey={}".format(
    os.getenv('API_KEY'))


def api_data(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict['results']


def ticker_list(stocks):
    newlist = []
    count = 0
    while count <= 60:
        newlist.append(
            {"ticker_name": stocks[count]["T"], "close_price": stocks[count]['c']})
        count += 1
    return newlist


def convert_symbol_to_company(ticker_list):
    stock_list = []
    for ticker in ticker_list:
        current_ticker = yf.Ticker(ticker['ticker_name'])
        stock_list.append({
            'symbol': ticker['ticker_name'],
            "org_name": current_ticker.info['longName'],
            "current_price": ticker['close_price']
        })
    return stock_list


@stock_route.route('/allstocks')
def list_of_stock():
    return api_data(polygon_API)


@stock_route.route('/<int:id>')
def stock(id):
    stock = Stock.query.get_or_404(id)
    return stock.to_dict()


@stock_route.route('/addstock', methods=["POST"])
def add_stocks():
    db_stocks = []
    aggs = convert_symbol_to_company(ticker_list(api_data(polygon_API)))
    for stock_currated in aggs:
        all_stocks = db.session.query(Stock.id).filter_by(
            symbol=stock_currated['symbol']).first() is not None
        if all_stocks == True:
            print("Already in DB")
        elif all_stocks == False:
            new_stock = Stock(
                org_name=stock_currated['org_name'],
                symbol=stock_currated['symbol'],
                current_price=stock_currated['current_price']
            )
            db_stocks.append(new_stock)
            db.session.add(new_stock)
            db.session.commit()
        else:
            print("Stock Symbol Not Found")
    return [stock_db.to_dict() for stock_db in db_stocks], {'message': "Sucess 200"}
