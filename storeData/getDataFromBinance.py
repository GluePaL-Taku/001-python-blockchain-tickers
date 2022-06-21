# for binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json

## for password
# import sys
# sys.path.append("../secret")
# import binance_password
## From secret/binance_password.py module
# api_key = binance_password.api_key
# api_secret = binance_password.api_secret

client = Client(api_key, api_secret)

def getBinanceAllTickers():
    return json.dumps(client.get_all_tickers())
