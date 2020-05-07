import os
from urllib.parse import urlencode
import requests
import json
import hashlib
import hmac
from time import time
from decimal import ROUND_DOWN,Context

main_path_data = os.path.abspath("./data")


########################     ALFA    ##########################
def alfa(val1, val2, price, amount):
    #####  direction  (buy  / sell)


    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
        if val1 == 'USD' or val1 == 'USDT':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass
    elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
        if val1 == 'BTC':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass



    tickers_all = ['BTC_USD', 'PZM_USD', 'ETH_USD', 'ETH_USDT', 'PZM_BTC', 'ETH_BTC']

    parametr1 = "{}_{}".format(val1, val2)
    parametr2 = "{}_{}".format(val2, val1)

    for i in tickers_all:
        if i == parametr1:
            para = i
            pass
        elif i == parametr2:
            para = i
            pass

    urll = 'https://btc-alpha.com/api/v1/pairs/'
    respo = requests.request("GET", urll)
    examm = respo.json()

    dec_val = para.split('_')

    for i in examm:
        if i['currency2'] == dec_val[1] and i['currency1'] == dec_val[0]:
            # amount = round(float(amount), int(i['price_precision']))
            amount = Context(prec=(i['price_precision'] + 2), rounding=ROUND_DOWN).create_decimal(amount)
            amount = float(amount)
            pass
        else:
            pass

    def keys():
        if os.path.isfile(main_path_data + "\\keys.json"):
            pass
        else:

            dictionary = {"1": {"key": "Api key",
                                "api": "Api secret"},
                          "2": {"key": "Api key",
                                "api": "Api secret"},
                          "3": {"key": "Api key",
                                "api": "Api secret"},
                          "4": {"key": "Chat id", "api": "Token"}}

            keys1 = json.dumps(dictionary, indent=4)
            with open(main_path_data + "\\keys.json", "w") as outfile:
                outfile.write(keys1)
                outfile.close()
                pass

    keys()

    a_file = open(main_path_data + "\\keys.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    input1 = json_object["1"]['key']
    input2 = json_object["1"]['api']

    if input1 != "Api key" and input2 != "Api secret":
        # Свой класс исключений
        class ScriptError(Exception):
            pass

        class ScriptQuitCondition(Exception):
            pass



        print('direction  :', direction)
        print('para  :', para)
        print('amount  :', amount)
        print('price  :', price)

        order = {
            'type': direction,
            'pair': para,
            'amount': str(amount),
            'price': price
        }

        def get_auth_headers(self, data):
            msg = input1 + urlencode(sorted(data.items(), key=lambda val: val[0]))
            sign = hmac.new(input2.encode(), msg.encode(), digestmod='sha256').hexdigest()

            return {
                'X-KEY': input1,
                'X-SIGN': sign,
                'X-NONCE': str(int(time() * 1000)),
            }

        response = requests.post('https://btc-alpha.com/api/v1/order/', data=order, headers=get_auth_headers({}, order))

        def resm():
            try:
                # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
                obj = json.loads(response.text)
                # Смотрим, есть ли в полученном объекте ключ "error"
                if 'error' in obj and obj['error']:
                    return obj['error']
                    # Если есть, выдать ошибку, код дальше выполняться не будет
                    # raise ScriptError(obj['error'])
                # Вернуть полученный объект как результат работы ф-ции
                return obj['success']
            except ValueError:
                # Если не удалось перевести полученный ответ (вернулся не JSON)
                return ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
                # raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)

        return resm()

    else:
        return ["ОШИБКА"]

########################     HOT    ##########################
def hot(val1, val2, price, amount):
  #####  direction  (buy  / sell)

  if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
      if val1 == 'USD' or val1 == 'USDT':
          direction = 2
          pass
      else:
          direction = 1
          pass
  elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
      if val1 == 'BTC':
          direction = 2
          pass
      else:
          direction = 1
          pass

  tickers_all = ['BTC/USD', 'BTC/USDT', 'PZM/USDT', 'ETH/USD', 'ETH/USDT', 'PZM/BTC', 'ETH/BTC']

  parametr1 = "{}/{}".format(val1, val2)
  parametr2 = "{}/{}".format(val2, val1)

  for i in tickers_all:
    if i == parametr1:
      para = i
      pass
    elif i == parametr2:
      para = i
      pass

  # print('PARA :', para)

  urll = 'https://api.hotbit.io/api/v1/market.list'
  respo = requests.request("GET", urll)
  examm = respo.json()


  dec_val = para.replace('/', '')

  for i in examm['result']:
      if i['name'] == dec_val:
          # print(i['stock_prec']+2)
          # print(type(i['stock_prec']))
          amount = Context(prec=(i['stock_prec']+2), rounding=ROUND_DOWN).create_decimal(amount)
          amount = float(amount)
          # print(amount)
          # amount = round(float(amount), int(i['stock_prec']))
          pass
      else:
          pass


  def keys():
    if os.path.isfile(main_path_data + "\\keys.json"):
      pass
    else:

      dictionary = {"1": {"key": "Api key",
                          "api": "Api secret"},
                    "2": {"key": "Api key",
                          "api": "Api secret"},
                    "3": {"key": "Api key",
                          "api": "Api secret"},
                    "4": {"key": "Chat id", "api": "Token"}}

      keys1 = json.dumps(dictionary, indent=4)
      with open(main_path_data + "\\keys.json", "w") as outfile:
        outfile.write(keys1)
        outfile.close()
        pass
  keys()

  a_file = open(main_path_data + "\\keys.json", "r")
  json_object = json.load(a_file)
  a_file.close()

  input1 = json_object["3"]['key']
  input2 = json_object["3"]['api']


  if input1 != "Api key" and input2 != "Api secret":
      # Свой класс исключений
      class ScriptError(Exception):
          pass

      class ScriptQuitCondition(Exception):
          pass



      msg = "amount={}&api_key={}&isfee=0&market={}&price={}&side={}&secret_key={}".format(
          amount, input1, para, price, direction, input2)

      # print("####   MSG  :",msg)
      sign = hashlib.md5(msg.encode()).hexdigest().upper()
      url2 = 'https://api.hotbit.io/api/v1/order.put_limit?amount={}&api_key={}&isfee=0&market={}&price={}&side={}&sign={}'.format(amount, input1, para, price, direction,sign)

      # print("####   url2  :", url2)

      response = requests.request("GET", url2)
      # exam2 = response.json()

      def resm():
        try:
          # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
          obj = json.loads(response.text)
          print('obj :', obj)
          # Смотрим, есть ли в полученном объекте ключ "error"
          if 'error' in obj and obj['error']:
            return obj['error']['message']
            # Если есть, выдать ошибку, код дальше выполняться не будет
            # raise ScriptError(obj['error'])
          # Вернуть полученный объект как результат работы ф-ции
          return obj['result']['id']
        except ValueError:
          # Если не удалось перевести полученный ответ (вернулся не JSON)
          return ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
          # raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)

      return resm()

  else:
    return ["ОШИБКА"]


#######################     Live    ##########################
def live(val1, val2, price, amount):
    #####  direction  (buy  / sell)
    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
        if val1 == 'USD' or val1 == 'USDT':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass
    elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
        if val1 == 'BTC':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass

    tickers_all = ['BTC/USD', 'PZM/USD', 'PZM/USDT', 'ETH/USD', 'ETH/USDT', 'PZM/BTC', 'ETH/BTC']

    parametr1 = "{}/{}".format(val1, val2)
    parametr2 = "{}/{}".format(val2, val1)

    for i in tickers_all:
        if i == parametr1:
            para = i
            pass
        elif i == parametr2:
            para = i
            pass

    url = 'https://api.livecoin.net/exchange/restrictions'
    respo = requests.request("GET", url)
    examm = respo.json()

    for i in examm['restrictions']:
        if i['currencyPair'] == para:
            # amount = round(float(amount), int(i['priceScale']))
            amount = Context(prec=(i['priceScale'] + 2), rounding=ROUND_DOWN).create_decimal(amount)
            amount = float(amount)
            pass
        else:
            pass


    def keys():
        if os.path.isfile(main_path_data + "\\keys.json"):
            pass
        else:

            dictionary = {"1": {"key": "Api key",
                                "api": "Api secret"},
                          "2": {"key": "Api key",
                                "api": "Api secret"},
                          "3": {"key": "Api key",
                                "api": "Api secret"},
                          "4": {"key": "Chat id", "api": "Token"}}

            keys1 = json.dumps(dictionary, indent=4)
            with open(main_path_data + "\\keys.json", "w") as outfile:
                outfile.write(keys1)
                outfile.close()
                pass

    keys()

    a_file = open(main_path_data + "\\keys.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    input1 = json_object["2"]['key']
    input2 = json_object["2"]['api']


    if input1 != "Api key" and input2 != "Api secret":
        # Свой класс исключений
        class ScriptError(Exception):
            pass

        class ScriptQuitCondition(Exception):
            pass



        print('direction  :', direction)
        print('para  :', para)
        print('amount  :', amount)
        print('price  :', price)

        order = {
            'currencyPair': para,
            'quantity': str(amount),
            'price': price
        }
        order2 = urlencode(sorted(order.items(), key=lambda val: val[0]))

        def get_auth_headers(self, data):
            # msg = input1 + urlencode(sorted(data.items(), key=lambda val: val[0]))
            msg = urlencode(sorted(data.items(), key=lambda val: val[0]))
            sign = hmac.new(input2.encode(), msg=msg.encode(), digestmod='sha256').hexdigest().upper()

            return {
                'Api-key': input1,
                'Sign': sign,
                "Content-type": "application/x-www-form-urlencoded"
            }


        if direction == 'sell':
            response = requests.post('https://api.livecoin.net/exchange/selllimit', data=order2,
                                     headers=get_auth_headers({}, order))
        #     /exchange/selllimit   /exchange/buylimit

        else:
            response = requests.post('https://api.livecoin.net/exchange/buylimit', data=order2,
                                     headers=get_auth_headers({}, order))

        def resm():
            try:
                # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
                obj = json.loads(response.text)

                # print("1", obj)
                # print("2", obj['success'])

                # Смотрим, есть ли в полученном объекте ключ "error"
                if obj['success'] == False:
                    return obj['exception']
                    # Если есть, выдать ошибку, код дальше выполняться не будет
                    # raise ScriptError(obj['error'])
                # Вернуть полученный объект как результат работы ф-ции
                return obj['success']
            except ValueError:
                # Если не удалось перевести полученный ответ (вернулся не JSON)
                return ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
                # raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)

        return resm()

    else:
        return ["ОШИБКА"]


# print(hot('PZM', 'USDT', '0.03293215', '600.355276494'))
# print(hot('ETH', 'BTC', '9000', '0.03'))