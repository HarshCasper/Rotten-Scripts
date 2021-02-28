# Imports
import yfinance as yf
from datetime import date
import sys

# Get Stock Market Data Function


def get_stock_data(freq, start, end, stock_name):
    tickerSymbol = stock_name
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period=freq, start=start, end=end)
    return tickerDf


if __name__ == "__main__":
    while True:
        freq = input(
            "Please frequency at which to gather the data; common options would include ‘1d’ (daily), ‘1mo’ (monthly), ‘1y’ (yearly): ")
        if freq not in ["1d", "1mo", "1y"]:
            print("Please enter the correct frequency")
            userkey = input("press 1 to try again or 0 to exit:")
            if userkey == "0":
                sys.exit()
        else:
            break
    while True:
        start = input(
            "Please enter the start date in the following format Year-Month-Date: ")
        try:
            start = date(*map(int, start.split('-')))
            if (not start.isoformat()):
                print("Error: must be format yyyy-mm-dd ")
                userkey = input("press 1 to try again or 0 to exit:")
                if userkey == "0":
                    sys.exit()
            else:
                break
        except:
            print("Error: must be format yyyy-mm-dd ")

    while True:
        end = input(
            "Please enter the end date in the following format Year-Month-Date: ")
        try:
            end = date(*map(int, end.split('-')))
            if (not end.isoformat()):
                print("Error: must be format yyyy-mm-dd ")
                userkey = input("press 1 to try again or 0 to exit:")
                if userkey == "0":
                    sys.exit()
            else:
                break
        except:
            print("Error: must be format yyyy-mm-dd ")
    while True:
        stock_name = input("Please enter the name of the stock: ")
        try:
            data = get_stock_data(freq, start, end, stock_name)
            break
        except:
            print(get_stocka_data(freq, start, end, stock_name))
    for index, row in data.iterrows():
        print("Date: {}--------------------".format(index))
        print("     Opens at : {}".format(row.Open))
        print("     Close at : {}".format(row.Close))
        print("     Highest : {}".format(row.High))
        print("     Low: {} ".format(row.Low))
