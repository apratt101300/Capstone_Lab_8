import requests
from pprint import pprint


bitcoins = int(input("How many bitcoins would you like to convert to USD? "))

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url).json()

bitcoin_price_USD = response['bpi']['USD']['rate_float']

print(bitcoin_price_USD)

result = bitcoins * bitcoin_price_USD

txt = "{bitcoins} Bitcoins is {result:,.2f} USD."

print(txt.format(bitcoins = bitcoins, result = result))