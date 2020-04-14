from random import choice
import os
import requests
from time import sleep
import time
from urllib.parse import urlparse
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from fake_useragent import UserAgent

# {'ETH/BTC': {'buy': '0.02288499', 'close': '0.022886',
# 'high': '0.02346957', 'last': '0.022886', 'low': '0.022477', 'open': '0.02335598', 'sell': '0.0229048', 'symbol': 'ETH_BTC', 'vol': '55394.369'}, 'BTC/USD': {'buy': '6950.45', 'close': '6999.49', 'high': '7398.9', 'last': '6999.49', 'low': '6932.37', 'open': '7398.26', 'sell': '7001.02', 'symbol': 'BTC_USD', 'vol': '2.731829'}, 'USDT/USD': {'buy': '1.0197', 'close': '1.0199', 'high': '1.025', 'last': '1.0199', 'low': '1.0083', 'open': '1.0103', 'sell': '1.02', 'symbol': 'USDT_USD', 'vol': '20509.22'}, 'BTC/USDT': {'buy': '6890.15', 'close': '6890.77', 'high': '7340', 'last': '6890.77', 'low': '6859.64', 'open': '7338.07', 'sell': '6890.78', 'symbol': 'BTC_USDT', 'vol': '165939.455064'}, 'ETH/USDT': {'buy': '157.63', 'close': '157.64', 'high': '171.44', 'last': '157.64', 'low': '156.27', 'open': '171.11', 'sell': '157.68', 'symbol': 'ETH_USDT', 'vol': '2889392.84627'}, 'ETH/USD': {'buy': '161.91', 'close': '161.94', 'high': '172.58', 'last': '161.94', 'low': '157.15', 'open': '171.43', 'sell': '165.16', 'symbol': 'ETH_USD', 'vol': '151.889556'}, 'LTC/BTC': {'buy': '0.006148', 'close': '0.006154', 'high': '0.006398', 'last': '0.006154', 'low': '0.00608', 'open': '0.0063', 'sell': '0.006159', 'symbol': 'LTC_BTC', 'vol': '25661.2008'}, 'XRP/BTC': {'buy': '0.00002719', 'close': '0.00002723', 'high': '0.00002783', 'last': '0.00002723', 'low': '0.00002643', 'open': '0.00002718', 'sell': '0.00002745', 'symbol': 'XRP_BTC', 'vol': '39738771.3'}, 'BCH/BTC': {'buy': '0.034036', 'close': '0.034265', 'high': '0.035697', 'last': '0.034265', 'low': '0.03374', 'open': '0.03569', 'sell': '0.034718', 'symbol': 'BCH_BTC', 'vol': '3607.209'}}



def loadRSS():

    file1 = open("proxies.txt", "r")
    PROXIES2 = file1.readlines()


    url1 = {'BTC/USD':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USD&limit=10&interval=1e-8'}
    url2 = {'USDT/USD':'https://api.hotbit.io/api/v1/order.depth?market=USDT/USD&limit=10&interval=1e-8'}
    url3 = {'ETH/USD':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USD&limit=10&interval=1e-8'}
    url4 = {'ETH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=ETH/BTC&limit=10&interval=1e-8'}
    url5 = {'LTC/BTC':'https://api.hotbit.io/api/v1/order.depth?market=LTC/BTC&limit=10&interval=1e-8'}
    url6 = {'BTC/USDT':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USDT&limit=10&interval=1e-8'}
    url7 = {'ETH/USDT':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USDT&limit=10&interval=1e-8'}
    url8 = {'XRP/BTC':'https://api.hotbit.io/api/v1/order.depth?market=XRP/BTC&limit=10&interval=1e-8'}
    url9 = {'ETH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=ETH/BTC&limit=10&interval=1e-8'}
    url10 = {'BCH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=BCH/BTC&limit=10&interval=1e-8'}



    urls = [url1, url2, url3,
            url4, url5, url6,url7,url8,url9,url10]
    hot = {}

    def set_proxy(session, proxy_candidates=PROXIES2, verify=False):
        """
        Configure the session to use one of the proxy_candidates.  If verify is
        True, then the proxy will have been verified to work.
        """
        while True:
            proxy = choice(proxy_candidates)
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

    def scrape_page(k, url):
        ua = UserAgent()
        session = requests.Session()
        session.headers = {'User-Agent': ua.random}
        set_proxy(session)


        while True:
            try:
                resp = session.get(url)
                v = resp.json()
                # data.update({k: resp.json()})


                hot.update({k: {'sell': [float(v['result']['asks'][0][0]), float(v['result']['asks'][0][1])], 'buy':[float(v['result']['bids'][0][0]), float(v['result']['bids'][0][1])]}})


                break
            except Exception as e:
                session.headers = {'User-Agent': ua.random}
                set_proxy(session, verify=True)
                sleep(0.1)

    for i in urls:
        for k, item in i.items():
            scrape_page(k, item)


    return hot


if __name__ == "__main__":
    start = time.process_time()
    start11 = time.process_time()
    print(loadRSS())
    print('HOT start TIME : ',(time.process_time() - start))