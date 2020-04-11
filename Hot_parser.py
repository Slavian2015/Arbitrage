import string

import requests
import json



# {'ETH/BTC': {'buy': '0.02288499', 'close': '0.022886', 'high': '0.02346957', 'last': '0.022886', 'low': '0.022477', 'open': '0.02335598', 'sell': '0.0229048', 'symbol': 'ETH_BTC', 'vol': '55394.369'}, 'BTC/USD': {'buy': '6950.45', 'close': '6999.49', 'high': '7398.9', 'last': '6999.49', 'low': '6932.37', 'open': '7398.26', 'sell': '7001.02', 'symbol': 'BTC_USD', 'vol': '2.731829'}, 'USDT/USD': {'buy': '1.0197', 'close': '1.0199', 'high': '1.025', 'last': '1.0199', 'low': '1.0083', 'open': '1.0103', 'sell': '1.02', 'symbol': 'USDT_USD', 'vol': '20509.22'}, 'BTC/USDT': {'buy': '6890.15', 'close': '6890.77', 'high': '7340', 'last': '6890.77', 'low': '6859.64', 'open': '7338.07', 'sell': '6890.78', 'symbol': 'BTC_USDT', 'vol': '165939.455064'}, 'ETH/USDT': {'buy': '157.63', 'close': '157.64', 'high': '171.44', 'last': '157.64', 'low': '156.27', 'open': '171.11', 'sell': '157.68', 'symbol': 'ETH_USDT', 'vol': '2889392.84627'}, 'ETH/USD': {'buy': '161.91', 'close': '161.94', 'high': '172.58', 'last': '161.94', 'low': '157.15', 'open': '171.43', 'sell': '165.16', 'symbol': 'ETH_USD', 'vol': '151.889556'}, 'LTC/BTC': {'buy': '0.006148', 'close': '0.006154', 'high': '0.006398', 'last': '0.006154', 'low': '0.00608', 'open': '0.0063', 'sell': '0.006159', 'symbol': 'LTC_BTC', 'vol': '25661.2008'}, 'XRP/BTC': {'buy': '0.00002719', 'close': '0.00002723', 'high': '0.00002783', 'last': '0.00002723', 'low': '0.00002643', 'open': '0.00002718', 'sell': '0.00002745', 'symbol': 'XRP_BTC', 'vol': '39738771.3'}, 'BCH/BTC': {'buy': '0.034036', 'close': '0.034265', 'high': '0.035697', 'last': '0.034265', 'low': '0.03374', 'open': '0.03569', 'sell': '0.034718', 'symbol': 'BCH_BTC', 'vol': '3607.209'}}
url = 'https://api.hotbit.io/api/v1/allticker'
res = requests.request("GET", url)
exam2 = res.json()



val = ['BTC_USD','ETH_USD','USDT_USD','BTC_USDT','ETH_USDT','XRP_BTC','ETH_BTC','LTC_BTC','BCH_BTC',]

# print(exam2)

hot = {}
for item in exam2['ticker']:
    for i in val:
        if item['symbol'] == i:
            k = i.translate(str.maketrans({'_': '/'}))
            hot.update({k: {'sell': [item['sell'], []], 'buy':[item['buy'], []]}})
        else:
            pass

print(hot)

# alfa = {
#     "USDBTC": {
#         "asks": [["7400"], ["7395"], ["7390"]],
#         "bids": [["7401"], ["7405"], ["7410"]],
#     }
# }