""" Powered by CoinDesk: https://www.coindesk.com/price/bitcoin """

import requests
from pprint import pprint

def main():
    bitcoins = get_number_bitcoins()
    api_response = get_bitcoin_api_response()
    bitcoin_price = get_bitcoin_price(api_response)
    result = calculate_USD(bitcoins, bitcoin_price)
    print_results(bitcoins, result)


def get_number_bitcoins():
    bitcoins = int(input("How many bitcoins would you like to convert to USD? "))
    return bitcoins


def get_bitcoin_api_response():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    return response


def get_bitcoin_price(response):
    bitcoin_price_USD = response['bpi']['USD']['rate_float']
    return bitcoin_price_USD


def calculate_USD(bitcoin, bitcoin_price):
    result = bitcoin * bitcoin_price
    return result


def print_results(bitcoins, result):
    txt = "{bitcoins} Bitcoins is {result:,.2f} USD."
    print(txt.format(bitcoins = bitcoins, result = result))


if __name__ == '__main__':
    main()