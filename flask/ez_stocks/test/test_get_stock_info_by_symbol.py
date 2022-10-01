from src.stock_info import *


def test_get_stock_info_correct_name_from_stock_symbol_DIS():
        
    stock_info = get_stock_info_by_symbol('DIS')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Disney' in stock_name

def test_get_stock_info_correct_name_from_stock_symbol_AAPL():

    stock_info = get_stock_info_by_symbol('AAPL')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Apple" in stock_name'

def test_get_stock_info_correct_name_from_stock_symbol_F():

    stock_info = get_stock_info_by_symbol('F')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Ford' in stock_name

def test_get_stock_info_correct_name_from_stock_symbol_MSFT():

    stock_info = get_stock_info_by_symbol('MSFT')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Microsoft' in stock_name
    
def test_get_stock_info_correct_name_from_stock_symbol_UBER():

    stock_info = get_stock_info_by_symbol('UBER')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Uber' in stock_name

def test_get_stock_info_correct_name_from_stock_symbol_LAC():

    stock_info = get_stock_info_by_symbol('LAC')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Lithium Americas Corp' in stock_name

def test_get_stock_info_correct_name_from_stock_symbol_LEVI():

    stock_info = get_stock_info_by_symbol('LEVI')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'Levi' in stock_name

def test_get_stock_info_correct_name_from_stock_symbol_NVDA():

    stock_info = get_stock_info_by_symbol('NVDA')  # returns alls stock info as a list
    stock_name = stock_info[0]  # first item == stock name

    assert 'NVIDIA Corp' in stock_name


