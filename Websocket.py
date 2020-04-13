import ssl
from typing import io

import websocket
import hashlib
import hmac
import json
import time
import os
from threading import Thread
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')
# INPUT API CREDENTIALS:
API_KEY = 'BtuWYH7DbtNLREeRUdfjfAxEiS71Lq6Wn2kyyoxS9zkiiVo2HtvZUg1CaMdJiuRHDUum9HutR'
API_SECRET = '4Bmhw5cz4f5QzoXt8XbnEMwoapYFirS6ozkD11Q7RiuYg7DidgTdnJLf8MUU8Bb6YAL5D5m65uvBR4JTavip5uA6'

# GLOBAL VARIABLES

channels = "book_BTC_USD"


# channels = {0: 'book_BTC_USD',
#             1: 'book_LTC_USD',
#             2: 'book_XRP_USD',
#             3: 'book_ETH_USD',
#             }
tickers = {}


def print_ticker():
    global ticker
    symbol = 'BTC_USD'
    while len(tickers) == 0:
        # wait for tickers to populate
        time.sleep(1)
    while True:
        # print BTCUSD ticker every second
        details = 'book_BTC_USD'
        print('%s:  Bid: %s, Ask: %s, Last Price: %s, Volume: %s'\
            %(symbol, details['type'], details['price'],\
            details['trades'], details['date']), end="\r", flush=True)
        time.sleep(1)

# def on_message(ws, message):
#     global channels, balances, tickers
#     data = json.loads(message)
#     # Handle events
#     if 'event' in data:
#         if data['event'] == 'info':
#             pass # ignore info messages
#         elif data['event'] == 'auth':
#             if data['status'] == 'OK':
#                 print('API authentication successful')
#             else:
#                 print(data['status'])
#         # Capture all subscribed channels
#         elif data['event'] == 'subscribed':
#             if data['channel'] == 'ticker':
#                 channels[data['chanId']] = [data['channel'], data['pair']]
#     # Handle channel data
#     else:
#         chan_id = data[0]
#         if chan_id in channels:
#             if 'ticker' in channels[chan_id]: # if channel is for ticker
#                 if data[1] == 'hb':
#                     pass
#                 else:
#                     # parse ticker and save to memory
#                     sym = channels[chan_id][1]
#
#                     print('sym : ', sym)
#                     ticker_raw = data[1]
#
#                     print('ticker_raw : ', ticker_raw)
#
#                     ticker_parsed = {
#                         'bid': ticker_raw[0],
#                         'ask': ticker_raw[2],
#                         'last_price': ticker_raw[6],
#                         'volume': ticker_raw[7],
#                     }
#                     tickers[sym] = ticker_parsed

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### API connection closed ###')
    os._exit(0)

def on_open(ws):



    print('API connected')
    # authenticate()
    print_ticker()
    # ws.send(json.dumps('book_BTC_USD'))
    #
    # # start printing the ticker
    # Thread(target=print_ticker).start()



def connect_api():
    global ws
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://btc-alpha.com",
                                on_open=on_open,
                            on_error = on_error,
                            on_close = on_close,
                            )

    on_open(ws)



    ws.run_forever()




# initialize api connection
connect_api()
