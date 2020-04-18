import os
import json
import requests
import pandas as pd

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)












main_path_data = os.path.abspath("./data")
# url = 'https://api.hotbit.io/api/v1/order.depth?market=BTC/USD&limit=3&interval=1e-8'
# # url = 'https://btc-alpha.com/api/v1/orderbook/BTC_USD'
# # # url = 'https://api.livecoin.net/exchange/all/order_book'
# res = requests.request("GET", url)
# exam = res.json()

# print (exam)
exam2 = {'error': None, 'result': {'asks': [['7200', '0.045755'], ['7210', '0.045756'], ['7220.02', '0.00351']], 'bids': [['7000', '0.00171'], ['6938.97', '0.002993'], ['6900.01', '0.024318']]}, 'id': 1587217383}

# print(exam2['result']['asks'])

###################################   LIVE      ###########################################
valuta = ['BTC/USD',
          # 'LTC/USD',
          # 'ETH/USD', 'XRP/USD', 'USDT/USD', 'BTC/USDT', 'ETH/USDT', 'XRP/BTC', 'ETH/BTC',
          # 'LTC/BTC', 'BCH/BTC', 'ZEC/BTC',
          ]
live = {}

for i in valuta:
    for k, v in exam.items():
        if k == i:
            del v['timestamp']
            v['sell'] = v.pop('asks')
            v['buy'] = v.pop('bids')
            live.update({k: {'sell': [[v['sell'][0][0], v['sell'][0][1]],[v['sell'][1][0], v['sell'][1][1]], [v['sell'][2][0], v['sell'][2][1]]],
                             'buy': [[v['buy'][0][0], v['buy'][0][1]], [v['buy'][1][0], v['buy'][1][1]], [v['buy'][2][0], v['buy'][2][1]]]}})



print(live)
###################################   LIVE      ###########################################




#####################     ALFA    ######################################
alfa = {'BTC/USD': {'sell': [[float(exam2['sell'][0]["price"]), float(exam2['sell'][0]["amount"])], [float(exam2['sell'][1]["price"]), float(exam2['sell'][1]["amount"])], [float(exam2['sell'][2]["price"]), float(exam2['sell'][2]["amount"])]],
                    'buy': [[float(exam2['buy'][0]["price"]), float(exam2['buy'][0]["amount"])],[float(exam2['buy'][1]["price"]), float(exam2['buy'][1]["amount"])],[float(exam2['buy'][2]["price"]), float(exam2['buy'][2]["amount"])]]
                    }}
#####################     ALFA    ######################################


hot = {'BTC/USD': {'sell': exam2['result']['asks'], 'buy':exam2['result']['bids']}}


birgi = {'hot': hot}



birga = []
valin = []
valout = []
rates = []
volume = []



def tab(item, value):

    for k,v in item.items():
        list = k.split('/')

        abc = [0,1,2]
        for i in abc:
            birga.append(value)
            valin.append(list[0])
            valout.append(list[1])
            r = ("{0:,.10f}".format(float((item[k]['buy'][i][0]))))
            r2 = r.replace(',', '')
            v = ("{0:,.10f}".format(float((item[k]['buy'][i][1]))))
            v2 = v.replace(',', '')
            rates.append(r2)
            volume.append(v2)


            birga.append(value)
            valin.append(list[1])
            valout.append(list[0])
            r21 = ("{0:,.10f}".format(float((item[k]['sell'][i][0]))))
            r22 = r21.replace(',', '')
            v21 = ("{0:,.10f}".format(float((item[k]['sell'][i][1]))))
            v22 = v21.replace(',', '')
            rates.append(r22)
            volume.append(v22)


    return


for value, item in birgi.items():
    tab(item,value)



dw = {'birga': birga, 'valin': valin, 'valout': valout, 'rates': rates, 'volume': volume}
df = pd.DataFrame(data=dw)

print(df)