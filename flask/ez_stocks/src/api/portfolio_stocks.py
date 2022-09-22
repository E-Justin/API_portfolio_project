from flask import Blueprint, jsonify, abort, request
from ..models import Portfolio_stocks, db, Portfolio, Stock

bp = Blueprint('portfolio_stocks', __name__, url_prefix = '/portfolio_stocks')

@bp.route('', methods=['GET'])
def index():
    """ get everything from portfolio_stocks"""
    portfolio_stocks = Portfolio_stocks.query.all()
    result = []
    for ps in portfolio_stocks:
        result.append(ps.serialize())
    return jsonify(result)

@bp.route('',  methods = ['POST'])
def create():
    """ create new portfolio_stock
        (add new stock to a portfolio) """
    if 'portfolio_id' not in request.json or 'stock_id' not in request.json:
        return abort(400)
    # check if portfolio_id exists
    Portfolio.query.get_or_404(request.json['portfolio_id'])
    # check if stock_id exists
    Stock.query.get_or_404(request.json['stock_id'])
    # construct portfolio_stocks
    ps = Portfolio_stocks(
        portfolio_id = request.json['portfolio_id'],
        stock_id = request.json['stock_id']
    )
    db.session.add(ps)
    db.session.commit()
    return(jsonify(ps.serialize()))

@bp.route('/<portfolio_id>', methods = ['GET']) 
def show(portfolio_id:int):
    """ get all stocks in a given portfolio"""
    result = []
    portfolio_stocks = Portfolio_stocks.query.filter_by(portfolio_id = portfolio_id)
    #ps = Portfolio_stocks.query.get_or_404(portfolio_id) #.query.filterby(portfolio_id = portfolio_id)
    for stock in portfolio_stocks:
        result.append(stock.serialize())

    return jsonify(result)
