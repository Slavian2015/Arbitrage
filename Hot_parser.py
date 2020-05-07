from random import choice
import os
import requests
from time import sleep
import time
from urllib.parse import urlparse
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from fake_useragent import UserAgent
import hashlib
import json
main_path_data = os.path.abspath("./data")

# {'ETH/BTC': {'buy': '0.02288499', 'close': '0.022886',
# 'high': '0.02346957', 'last': '0.022886', 'low': '0.022477', 'open': '0.02335598', 'sell': '0.0229048', 'symbol': 'ETH_BTC', 'vol': '55394.369'}, 'BTC/USD': {'buy': '6950.45', 'close': '6999.49', 'high': '7398.9', 'last': '6999.49', 'low': '6932.37', 'open': '7398.26', 'sell': '7001.02', 'symbol': 'BTC_USD', 'vol': '2.731829'}, 'USDT/USD': {'buy': '1.0197', 'close': '1.0199', 'high': '1.025', 'last': '1.0199', 'low': '1.0083', 'open': '1.0103', 'sell': '1.02', 'symbol': 'USDT_USD', 'vol': '20509.22'}, 'BTC/USDT': {'buy': '6890.15', 'close': '6890.77', 'high': '7340', 'last': '6890.77', 'low': '6859.64', 'open': '7338.07', 'sell': '6890.78', 'symbol': 'BTC_USDT', 'vol': '165939.455064'}, 'ETH/USDT': {'buy': '157.63', 'close': '157.64', 'high': '171.44', 'last': '157.64', 'low': '156.27', 'open': '171.11', 'sell': '157.68', 'symbol': 'ETH_USDT', 'vol': '2889392.84627'}, 'ETH/USD': {'buy': '161.91', 'close': '161.94', 'high': '172.58', 'last': '161.94', 'low': '157.15', 'open': '171.43', 'sell': '165.16', 'symbol': 'ETH_USD', 'vol': '151.889556'}, 'LTC/BTC': {'buy': '0.006148', 'close': '0.006154', 'high': '0.006398', 'last': '0.006154', 'low': '0.00608', 'open': '0.0063', 'sell': '0.006159', 'symbol': 'LTC_BTC', 'vol': '25661.2008'}, 'XRP/BTC': {'buy': '0.00002719', 'close': '0.00002723', 'high': '0.00002783', 'last': '0.00002723', 'low': '0.00002643', 'open': '0.00002718', 'sell': '0.00002745', 'symbol': 'XRP_BTC', 'vol': '39738771.3'}, 'BCH/BTC': {'buy': '0.034036', 'close': '0.034265', 'high': '0.035697', 'last': '0.034265', 'low': '0.03374', 'open': '0.03569', 'sell': '0.034718', 'symbol': 'BCH_BTC', 'vol': '3607.209'}}



def loadRSS():

    # file1 = open("proxies.txt", "r")
    # PROXIES2 = file1.readlines()
    prox = ['36.74.205.128:3128', '103.116.203.242:43520', '186.0.176.147:80', '128.199.150.150:47503',
            '41.78.243.189:53281', '46.19.225.141:8888', '190.166.249.44:37359', '41.78.243.194:53281']
    pro = ['94.154.208.248:80','89.252.12.88:80', '13.66.220.17:80', '104.45.11.83:80', '104.45.11.83:443']

    # url1 = {'BTC/USD':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USD&limit=3&interval=1e-8'}
    url2 = {'PZM/USDT':'https://api.hotbit.io/api/v1/order.depth?market=PZM/USDT&limit=3&interval=1e-8'}
    # url3 = {'ETH/USD':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USD&limit=3&interval=1e-8'}
    url4 = {'PZM/BTC':'https://api.hotbit.io/api/v1/order.depth?market=PZM/BTC&limit=3&interval=1e-8'}
    # url5 = {'LTC/BTC':'https://api.hotbit.io/api/v1/order.depth?market=LTC/BTC&limit=3&interval=1e-8'}
    # url6 = {'BTC/USDT':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USDT&limit=3&interval=1e-8'}
    # url7 = {'ETH/USDT':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USDT&limit=3&interval=1e-8'}
    # url8 = {'XRP/BTC':'https://api.hotbit.io/api/v1/order.depth?market=XRP/BTC&limit=3&interval=1e-8'}
    # url9 = {'ETH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=ETH/BTC&limit=3&interval=1e-8'}
    # url10 = {'BCH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=BCH/BTC&limit=3&interval=1e-8'}



    urls = [
        # url1,
            url2,
        # url3,
        url4,
            # url5, url6,
            # url7,
            # url8,
            # url9,
            # url10
            ]
    hot = {}

    def set_proxy(session, proxy_candidates=pro, verify=False):
        """
        Configure the session to use one of the proxy_candidates.  If verify is
        True, then the proxy will have been verified to work.
        """
        while True:
            proxy = choice(proxy_candidates)
            print("NEW   PROXY  HOT:", proxy)
            session.proxies = {urlparse(proxy).scheme: proxy}
            if not verify:
                return
            try:
                print(session.get('https://httpbin.org/ip').json())
                return
            except Exception:
                session.proxies = {urlparse(next(proxy)).scheme: proxy}
                print("EXCEPTION")
                pass

    def scrape_page():
        ua = UserAgent()
        session = requests.Session()
        session.headers = {'User-Agent': ua.random}
        set_proxy(session)

        while True:
            try:
                for i in urls:
                    for k, item in i.items():
                        resp = session.get(item)
                        v = resp.json()

                        hot.update({k: {
                                'sell': [[v['result']['asks'][0][0], v['result']['asks'][0][1]],
                                [v['result']['asks'][1][0], (float(v['result']['asks'][0][1]) + float(v['result']['asks'][1][1]))],
                                [v['result']['asks'][2][0], (float(v['result']['asks'][0][1]) + float(v['result']['asks'][1][1]) + float(v['result']['asks'][2][1]))]],
                                'buy':[[v['result']['bids'][0][0], v['result']['bids'][0][1]],
                                       [v['result']['bids'][1][0], (float(v['result']['bids'][0][1]) + float(v['result']['bids'][1][1]))],
                                       [v['result']['bids'][2][0], (float(v['result']['bids'][0][1]) + float(v['result']['bids'][1][1]) + float(v['result']['bids'][2][1]))]]



}})


                break
            except Exception as e:
                session.headers = {'User-Agent': ua.random}
                set_proxy(session, verify=True)
                sleep(0.1)


    scrape_page()

    # print(hot)
    return hot

def wallet_h():

    a_file = open(main_path_data + "\\keys.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    input1 = json_object["3"]['key']
    input2 = json_object["3"]['api']

    if input1 != "Api key" and input2 != "Api secret":
        str2hash = 'api_key={}&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","PZM","XLM"]&secret_key={}'.format(input1, input2)
        result = hashlib.md5(str2hash.encode())

        sign = result.hexdigest().upper()

        url = 'https://api.hotbit.io/api/v1/balance.query?api_key={}&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","PZM","XLM"]&sign={}'.format(input1,
            sign)

        res = requests.request("GET", url)
        exam = res.json()

        print(exam)

        wallet_h = {}

        for i in exam['result']:
            wallet_h.update({i: exam['result'][i]['available']})

        return wallet_h
    else:
        return {}


if __name__ == "__main__":
    start = time.process_time()
    start11 = time.process_time()
    print(wallet_h())
    print('HOT start TIME : ',(time.process_time() - start))