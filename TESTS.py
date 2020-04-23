# # import os
# import json
# import requests
# # import pandas as pd
# # import dash_core_components as dcc
# # import dash_html_components as html
# # import dash_bootstrap_components as dbc
# # import dash_design_kit as ddk
# # import uuid
# # import dash_table
# # from app import dash_app
# # from VILKA import valuta
# import hashlib
#
# #
# # ##################################   SHOW ALL ROWS & COLS   ####################################
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.expand_frame_repr', False)
# # pd.set_option('max_colwidth', None)
#
#
#
#
#
#
# # import httplib
# # import urllib
# # import json
# # import hashlib
# # import hmac
# # from collections import OrderedDict
# #
# # server = "api.livecoin.net"
# # method = "/payment/balances"
# # api_key = "gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4"
# # secret_key = "dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG"
# #
# # data = OrderedDict([('currencyPair', 'BTC/USD')])
# #
# # encoded_data = urllib.urlencode(data)
# #
# # sign = hmac.new(secret_key, msg=encoded_data, digestmod=hashlib.sha256).hexdigest().upper()
# #
# # headers = {"Api-key": api_key, "Sign": sign}
# #
# # conn = httplib.HTTPSConnection(server)
# # conn.request("GET", method + '?' + encoded_data, '', headers)
# #
# # response = conn.getresponse()
# # data = json.load(response)
# # conn.close()
# #
# # print(data)
#
#
#
# ##########################################################################
#
#
# # # ключи API, которые предоставила exmo
# # global API_KEY
# # API_KEY = input1
# # # обратите внимание, что добавлена 'b' перед строкой
# # global API_SECRET
# # API_SECRET = input2
#
# import hmac
#
# api_key = "gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4"
# secret_key = "dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG"
#
#
# input1 = api_key
# input2 =secret_key
#
# # Свой класс исключений
# class ScriptError(Exception):
#     pass
#
# class ScriptQuitCondition(Exception):
#     pass
#
# msg = input1
# sign = hmac.new(input2.encode(), digestmod='sha256').hexdigest().upper()
# headers = {
#     'Api-key': input1,
#     'Sign': sign,
# }
# response = requests.get('https://api.livecoin.net/payment/balances', headers=headers)
#
#
# def resm():
#     try:
#         # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
#         obj = json.loads(response.text)
#         # Смотрим, есть ли в полученном объекте ключ "error"
#         if 'error' in obj and obj['error']:
#             # Если есть, выдать ошибку, код дальше выполняться не будет
#             raise ScriptError(obj['error'])
#         # Вернуть полученный объект как результат работы ф-ции
#         return obj
#     except ValueError:
#         # Если не удалось перевести полученный ответ (вернулся не JSON)
#         raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
#
#
# print(resm())
#
#
#
# resm = [{'type': 'trade', 'currency': 'BTC', 'value': 1}, {'type': 'trade', 'currency': 'ETH', 'value': 1}, {'type': 'trade', 'currency': 'WINGS', 'value': 0}]
# wallet_l = {}
#
#
# for i in resm:
#     if i['type'] == "trade" and i['value'] > 0:
#         wallet_l.update({i['currency']: i['value']})
#
# print(wallet_l)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # str2hash = 'api_key=9d9e97f9-78ff-12f4-6a354d870d40fc2b&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","XLM"]&secret_key=9ed49b83f87a4d27f71a25df023f78e9'
# # result = hashlib.md5(str2hash.encode())
# #
# # sign = result.hexdigest().upper()
# #
# # url = 'https://api.hotbit.io/api/v1/balance.query?api_key=9d9e97f9-78ff-12f4-6a354d870d40fc2b&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","XLM"]&sign={}'.format(sign)
# #
# # res = requests.request("GET", url)
# # exam = res.json()
# # print(exam)
# #
# # wallet_h = {}
# #
# # for i in exam['result']:
# #     wallet_h.update({i: exam['result'][i]['available']})
# #
# # print(wallet_h)
#
#
#
#
# ###########  ALFA ######################################################
# # def alfa_wallet(input1, input2):
# #
# #     import hmac
# #     from time import time
# #
# #
# #     # Свой класс исключений
# #     class ScriptError(Exception):
# #         pass
# #
# #
# #     class ScriptQuitCondition(Exception):
# #         pass
# #
# #
# #     def get_auth_headers(self):
# #         # print('input 1  :', input1)
# #         # print('input 2  :', input2)
# #
# #         msg = input1
# #         sign = hmac.new(input2.encode(), msg.encode(), digestmod='sha256').hexdigest()
# #
# #         return {
# #             'X-KEY': input1,
# #             'X-SIGN': sign,
# #             'X-NONCE': str(int(time() * 1000)),
# #         }
# #
# #
# #     response = requests.get('https://btc-alpha.com/api/v1/wallets/', headers=get_auth_headers({}))
# #
# #
# #     def resm():
# #         try:
# #             # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
# #             obj = json.loads(response.text)
# #             # Смотрим, есть ли в полученном объекте ключ "error"
# #             if 'error' in obj and obj['error']:
# #                 # Если есть, выдать ошибку, код дальше выполняться не будет
# #                 raise ScriptError(obj['error'])
# #             # Вернуть полученный объект как результат работы ф-ции
# #             return obj
# #         except ValueError:
# #             # Если не удалось перевести полученный ответ (вернулся не JSON)
# #             raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
# #
# #     return resm()
# # var = ['BTC_USD', 'LTC_USD', 'ETH_USD', 'XRP_USD', 'USD_USDT', 'BTC_USDT', 'ETH_USDT', 'XRP_BTC', 'ETH_BTC', 'LTC_BTC', 'BCH_BTC', 'ZEC_BTC']
# #
# # val1 = 'BTC'
# # val2 = 'USD'
# #
# # pair = (val1 +'_'+val2)
# # print(pair)
# #
# #
# # # ключи API, которые предоставила alfa
# # global API_KEY
# # API_KEY = 'BtuWYH7DbtNLREeRUdfjfAxEiS71Lq6Wn2kyyoxS9zkiiVo2HtvZUg1CaMdJiuRHDUum9HutR'
# # # обратите внимание, что добавлена 'b' перед строкой
# # global API_SECRET
# # API_SECRET = '4Bmhw5cz4f5QzoXt8XbnEMwoapYFirS6ozkD11Q7RiuYg7DidgTdnJLf8MUU8Bb6YAL5D5m65uvBR4JTavip5uA6'
# #
# # input1 = API_KEY
# # input2 = API_SECRET
# # print(alfa_wallet(input1, input2))
# #
# #
# # # def content2():
# # #     wallets = resm()
# # #     var = []
# # #     for k in wallets:
# # #         card_content = dbc.ListGroupItem(action=True,
# # #                                          style={'padding': '0', 'margin': '0', 'width': '100%',
# # #                                                 'text-align': 'center'},
# # #                                          children=ddk.Row(
# # #                                              style={'padding': '0', 'margin': '0', 'width': '100%',
# # #                                                     'text-align': 'center'},
# # #                                              children=[
# # #                                                  dbc.Col(style={'width': '50%', 'max-width': 'fit-content',
# # #                                                                 'max-height': 'fit-content',
# # #                                                                 # 'height': '100%',
# # #                                                                 'padding': '0px',
# # #                                                                 'vertical-align': '-webkit-baseline-middle',
# # #                                                                 'align-items': 'center',
# # #                                                                 'justify-content': 'center',
# # #                                                                 'margin': '0', 'textAlign': 'center',
# # #                                                                 'margin-left': '10px',
# # #                                                                 'margin-right': '10px'},
# # #                                                          children=html.P('{}  :'.format(str(k['currency'])),
# # #                                                                          style={'height': '100%',
# # #                                                                                 'max-height': 'fit-content',
# # #                                                                                 'vertical-align': '-webkit-baseline-middle'})),
# # #                                                  dbc.Col(style={'width': '50%',
# # #                                                                 'padding': '0px',
# # #                                                                 # 'height': '100%',
# # #                                                                 'max-width': '150px',
# # #                                                                 'align-items': 'center',
# # #                                                                 'justify-content': 'center',
# # #                                                                 'margin': '10px',
# # #                                                                 'max-height': 'fit-content',
# # #                                                                 'textAlign': 'center',
# # #                                                                 'vertical-align': '-webkit-baseline-middle',
# # #                                                                 },
# # #                                                          children=html.P('{}'.format(float(k['balance'])),
# # #                                                                          style={'height': '100%',
# # #                                                                                 'max-height': 'fit-content',
# # #                                                                                 'vertical-align': '-webkit-baseline-middle'}))]))
# # #         var.append(card_content)
# # #
# # #     return var
# #
# #
# #
# #
# # ###############  new ORDER  #################
# #
# # print()
#
# # def a_oreder():
# #     import hmac
# #     from time import time
# #
# #     # Свой класс исключений
# #     class ScriptError(Exception):
# #         pass
# #     class ScriptQuitCondition(Exception):
# #         pass
# #
# #
# #
# #
# #     order = {
# #         "type": 'buy',
# #         "pair": 'BTC_USD',
# #         "amount": '1.0',
# #         "price": '870.69'
# #     }
# #
# #     def get_auth_headers(self):
# #         msg = input1
# #         sign = hmac.new(input2.encode(), msg.encode(), digestmod='sha256').hexdigest()
# #         return {
# #             'X-KEY': input1,
# #             'X-SIGN': sign,
# #             'X-NONCE': str(int(time() * 1000)),
# #         }
# #
# #     response = requests.post('https://btc-alpha.com/api/v1/order/', data=order, headers=get_auth_headers(order))
# #
# #
# #     def resm():
# #         try:
# #             # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
# #             obj = json.loads(response.text)
# #             # Смотрим, есть ли в полученном объекте ключ "error"
# #             if 'error' in obj and obj['error']:
# #                 # Если есть, выдать ошибку, код дальше выполняться не будет
# #                 raise ScriptError(obj['error'])
# #             # Вернуть полученный объект как результат работы ф-ции
# #             return obj
# #         except ValueError:
# #             # Если не удалось перевести полученный ответ (вернулся не JSON)
# #             raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
# #
# #     return resm()
# #
# #
# # resm = {
# #   "success": 'true',
# #   "type": "buy",
# #   "date": 1483721079.51632,
# #   "oid": 11268,
# #   "price": 870.69000000,
# #   "amount": 0.00000000,
# #   "trades": [
# #     {
# #       "type": "sell",
# #       "price": 870.69000000,
# #       "o_id": 11266,
# #       "amount": 0.00010000,
# #       "tid": 6049
# #     }
# #   ]
# # }
import os
main_path_data = os.path.abspath("./data")
import json
# import A_parser
# import Hot_parser
# import Live_parser

import pandas as pd
from functools import reduce


print()
# print(val['Alfa'])

# val = {
#     'Alfa':A_parser.wallet_a(),
#     'Hot':Hot_parser.wallet_h(),
#     'Live':Live_parser.wallet_l(),
# }


##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

#
# Alfa={'BTCd': '1.00000000', 'USDTd': '10000.00000000', 'USDT': '5.00073249', 'USD': '2.48900000'}
# Hot={'XRP': '0', 'BTC': '0', 'LTC': '0', 'ZEC': '0.006', 'ETH': '0', 'USDT': '0', 'XLM': '0'}
# Live={}
#
#
#
# dfa = pd.DataFrame(Alfa.items(), columns=['Valuta', 'Alfa'])
# dfh = pd.DataFrame(Hot.items(), columns=['Valuta', 'Hot'])
# dfl = pd.DataFrame(Live.items(), columns=['Valuta', 'Live'])
#
# data_frames = [dfa, dfh, dfl]
# df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Valuta'],
#                                             how='outer'), data_frames).fillna('0')
#
#
#
# print(df_merged)

# df_all = pd.read_csv(main_path_data + "\\all_data.csv")
#
# print(df_all.loc[0])


a_file = open(main_path_data + "\\regim.json", "r")
json_object = json.load(a_file)
a_file.close()
print("  REGIM BEFORE :", '\n', json_object)


for i in json_object:
    print(i)
# json_object[['index']])