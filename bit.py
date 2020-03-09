#!/usr/bin/env python2.7


#################################
#	Author:			#
#	Sean-Michael Woerner	#
#################################

import requests
import json

#****DEFINITIONS*****************
ETH = 'ethereum'
BTC = 'bitcoin'
LTC = 'litecoin'
XRP = 'ripple'
STR = 'stellar'
#********************************


TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

def get_latest_crypto_price(crypto):
	response = requests.get(TICKER_API_URL+crypto)
	response_json = response.json()
	return float(response_json[0]['price_usd'])

ETH_USD = get_latest_crypto_price(ETH)
BTC_USD = get_latest_crypto_price(BTC)
LTC_USD = get_latest_crypto_price(LTC)
XRP_USD = get_latest_crypto_price(XRP)
STR_USD = get_latest_crypto_price(STR)

print "ETH current price: ",ETH_USD
print "BTC current price: ",BTC_USD
print "LTC current price: ",LTC_USD
print "XRP current price: ",XRP_USD
print "STR current price: ",STR_USD


