import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info["currentPrice"]

