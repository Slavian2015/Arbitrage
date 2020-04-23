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
            '108.177.235.174:3128', '125.27.251.206:50817', '191.252.221.204:80', '206.189.147.71:44344',
            '45.64.99.25:8080', '178.93.21.147:31384', '200.107.236.19:3128', '138.121.32.133:23492',
            '113.160.206.37:37194', '144.76.214.155:1080', '103.142.68.163:80', '176.9.62.77:80', '51.158.111.242:8811',
            '169.57.157.146:80', '78.46.81.7:1080', '103.220.207.242:32227', '82.119.170.106:8080', '191.252.58.19:80',
            '144.76.214.159:1080', '45.231.212.56:59688', '186.189.235.93:8080', '45.173.128.21:3128',
            '185.166.213.2:80', '200.255.122.170:8080', '118.179.76.45:8080', '188.40.183.185:1080',
            '85.10.219.103:1080', '185.166.212.190:80', '188.40.183.189:1080', '91.191.53.106:57073',
            '138.197.157.32:8080', '203.202.245.58:80', '188.40.183.188:1080', '88.198.50.103:8080',
            '186.216.81.21:31773', '181.129.127.234:57985', '117.58.241.164:52636', '181.118.167.104:80',
            '168.228.51.197:30188', '190.15.195.25:57412', '144.76.214.154:1080', '181.196.151.82:59612',
            '77.70.35.87:48198', '85.10.219.98:1080', '188.40.183.186:1080', '138.197.157.44:8080',
            '187.86.137.141:58628', '88.99.10.251:1080', '186.248.170.82:53281', '103.145.133.30:8080',
            '201.204.46.10:39371', '136.243.92.25:1080', '68.183.208.248:80', '185.166.213.7:80',
            '190.14.156.196:23500', '91.187.116.232:36908', '176.9.75.42:8080', '138.197.157.45:8080',
            '188.40.183.191:1080', '169.57.157.148:8123', '190.7.141.66:44945', '144.76.214.156:1080',
            '188.40.183.184:1080', '185.166.213.18:80', '154.16.202.22:8080', '207.154.231.212:8080',
            '194.26.180.142:80', '178.63.246.82:8118', '176.9.119.170:8080', '151.253.165.70:8080',
            '190.152.71.230:54354', '207.154.231.216:8080', '62.171.161.146:8080', '185.205.209.198:80',
            '138.197.157.60:3128', '185.166.213.246:80', '207.154.231.211:3128', '148.251.153.6:1080',
            '145.239.81.69:8080', '91.139.1.158:37504', '88.198.24.108:8080', '190.61.55.243:999',
            '144.76.214.157:1080', '207.154.231.213:8080', '144.76.214.152:1080', '138.185.246.239:55146',
            '144.76.214.158:1080', '191.240.152.133:80', '46.4.96.137:3128', '177.94.225.58:55674',
            '190.152.125.250:43133', '186.249.68.49:43228', '186.211.182.113:61548', '123.200.26.22:48280',
            '88.99.10.254:1080', '144.217.101.242:3129', '125.133.214.39:80', '110.77.134.106:8080',
            '165.22.97.210:8080', '102.164.220.152:40339', '45.248.138.210:59714', '177.66.255.9:33774',
            '109.245.239.125:55311', '103.141.108.161:3127', '209.97.159.125:3128', '168.205.222.49:57643',
            '118.174.232.60:34772', '177.67.203.130:32474', '202.138.236.35:53298', '169.239.223.136:49027',
            '113.53.230.167:80', '91.215.195.143:50876', '118.174.65.137:33122', '176.101.89.226:33470',
            '103.216.95.16:61755', '113.53.29.218:31829', '103.105.77.48:8181', '211.24.105.248:39784',
            '93.185.96.61:43749', '85.10.219.102:1080', '190.111.231.8:8080', '113.161.207.99:60626',
            '213.6.38.50:46812', '163.53.209.8:6666', '81.174.11.159:49733', '78.38.111.251:8080',
            '165.227.47.191:8118', '176.103.40.198:41439', '200.105.179.186:47232', '60.251.33.224:80',
            '159.138.1.185:80', '124.121.42.23:8213', '65.152.119.226:47831', '155.93.240.101:8080',
            '80.255.91.38:43360', '54.37.14.65:3129', '197.210.217.66:31512', '91.214.128.243:23500',
            '185.134.23.195:80', '185.255.178.206:7787', '110.74.219.189:57054', '84.53.247.204:53281',
            '92.114.234.206:46685', '47.91.217.100:80', '159.8.114.34:8123', '62.106.122.90:58046', '159.138.21.170:80',
            '195.239.178.110:55913', '118.97.29.210:30701', '117.196.236.221:7999', '96.87.16.153:41344',
            '92.112.123.207:46189', '96.9.77.71:8080', '182.52.51.43:49699', '91.219.56.221:8080',
            '41.223.155.118:53281', '132.255.212.203:30154', '5.23.103.98:42328', '103.91.128.126:33746',
            '117.254.60.203:50818', '170.81.35.26:36681', '81.161.61.88:31692', '187.111.160.29:40098',
            '115.42.64.227:8080', '41.169.78.42:54372', '181.112.40.114:44739', '205.158.57.2:53281',
            '201.20.98.22:37596', '178.128.95.40:8118', '218.161.36.89:53438', '103.61.101.74:47177',
            '45.177.133.140:8080', '94.228.82.170:59280', '180.253.121.148:8080', '149.129.40.231:3128',
            '101.255.40.18:31558', '81.95.230.211:3128', '45.115.171.252:41945', '195.138.92.152:35245',
            '119.2.54.204:44860', '125.27.251.79:60832', '200.89.159.153:8080', '202.160.147.2:57974',
            '103.216.82.190:6666', '41.65.146.38:8080', '124.219.176.139:39589', '203.207.52.206:8085',
            '45.146.212.2:11999', '124.120.236.63:8213', '213.32.252.120:45728', '111.95.23.104:3128',
            '118.175.93.148:58483', '103.239.254.114:32325', '110.44.133.135:3128', '178.210.129.228:41258',
            '86.57.136.230:3128', '103.240.161.109:6666', '103.239.254.70:61967', '46.151.145.4:53281',
            '1.0.187.200:8080', '185.32.120.177:60724', '201.49.235.88:23500', '62.133.130.206:3128',
            '36.68.22.96:8080', '121.144.19.44:8080', '201.123.117.195:8080', '203.19.88.59:80', '159.224.83.100:8080',
            '179.127.241.151:59477', '200.68.13.26:50444', '187.44.160.234:50588', '203.19.88.51:80', '51.38.86.0:8080',
            '195.4.164.127:8080', '181.117.176.236:61358', '222.252.25.168:8080', '179.124.19.9:50664',
            '167.172.188.118:3128', '103.36.11.26:8080', '91.67.240.32:3128', '177.137.203.178:60771',
            '95.0.66.102:8081', '203.202.245.62:80', '35.220.131.188:80', '170.0.54.234:49912', '188.191.165.92:8080',
            '154.73.85.1:43388', '194.213.43.166:38170', '45.235.87.65:53781', '187.105.218.7:34752',
            '191.240.152.135:80', '94.230.149.73:46220', '202.143.121.245:8080', '181.129.140.226:36733',
            '185.138.69.110:39274', '94.130.20.85:31288', '186.219.214.30:40456', '190.2.249.74:3128',
            '200.55.218.202:53281', '103.112.212.30:83', '128.199.72.10:1080', '176.235.148.38:9090',
            '103.130.172.98:8080', '180.211.183.178:32009', '185.189.199.75:23500', '178.63.114.21:3128',
            '190.96.91.243:8080', '197.210.124.0:80', '94.130.179.24:8008', '51.107.71.159:80', '201.76.3.230:8080',
            '187.60.161.75:8081', '177.139.176.242:65301', '74.59.132.126:49073', '180.93.14.86:8080',
            '200.7.207.162:3127', '186.46.120.230:59282', '200.236.221.242:52426', '177.136.168.13:43626',
            '181.191.106.124:43716', '31.209.110.159:55166', '103.126.13.10:45338', '85.217.137.77:3128',
            '68.183.234.42:8080', '200.29.109.112:44749', '185.202.165.1:53281', '200.27.110.28:38881',
            '3.124.80.57:80', '103.213.236.11:82', '179.108.123.210:35436', '45.225.188.94:36707', '140.82.60.35:3128',
            '45.168.72.39:40373', '190.144.116.34:36742', '80.187.140.26:8080', '191.240.152.130:80',
            '182.48.81.222:46157', '103.221.254.102:49614', '138.122.140.35:3128', '201.234.185.147:37743',
            '186.226.172.165:60711', '217.196.81.221:51349', '167.86.89.60:3128', '181.211.245.74:44267',
            '203.76.149.106:8080', '185.50.56.230:32231', '178.63.246.85:8118', '190.128.26.98:56204',
            '186.226.183.170:30698', '190.152.223.2:37994', '113.53.120.97:8080', '185.99.64.75:61503',
            '103.142.68.161:80', '85.187.17.39:53281', '200.108.183.2:8080', '45.114.38.25:8080', '195.4.164.127:8080',
            '212.29.236.66:80', '93.189.89.39:80', '185.166.213.246:80', '185.166.213.2:80', '188.166.2.49:1081',
            '34.249.53.25:8080', '82.81.169.142:80', '124.121.42.23:8213', '124.121.99.78:8080', '219.93.16.182:42436',
            '203.142.58.69:38732', '210.48.204.134:46669', '217.64.109.231:45282', '41.75.123.49:41263',
            '41.87.29.130:8080', '94.242.213.96:8118', '41.190.92.84:32997', '109.75.67.183:44151',
            '185.104.252.9:9090', '154.66.110.90:57393', '41.254.44.62:55277', '78.62.214.242:60678',
            '94.232.126.225:48235', '82.135.148.201:8081', '213.246.30.188:8080', '41.217.219.53:31398',
            '41.190.95.20:56167', '195.158.109.248:50330', '41.60.236.44:56835', '80.82.69.76:80',
            '113.160.235.49:8080', '41.79.60.11:8080', '178.254.138.18:6666', '109.92.222.170:53281',
            '105.179.10.210:8080', '46.8.115.218:8080', '46.239.40.167:8080', '178.132.220.241:8080',
            '87.250.109.174:8080', '117.2.121.203:8080', '195.178.56.33:8080', '77.105.12.95:6666',
            '91.210.136.202:8080', '113.161.68.146:8080', '78.137.88.158:8080', '77.247.89.253:8080',
            '212.72.222.157:8080', '196.2.15.68:8080', '88.199.164.140:8080', '41.63.0.41:8888', '203.177.127.198:8080',
            '41.60.218.10:8080', '137.59.120.58:8080', '103.46.210.34:8080', '196.27.106.112:8080', '120.28.57.114:80',
            '200.127.155.86:8080', '190.116.183.196:8080', '190.116.183.197:8080', '118.27.6.16:8080',
            '118.27.12.201:8888', '54.77.37.161:8080', '31.146.188.252:8080', '151.22.181.222:8080', '51.79.52.62:8080',
            '109.168.18.50:80', '185.111.249.65:8080', '110.44.133.135:3128', '51.158.181.161:3128',
            '80.240.201.8:8080', '168.131.152.123:3128', '45.70.196.136:999', '181.198.42.229:8080', '186.47.82.138:80',
            '178.135.51.30:8080', '185.107.50.1:1234', '212.98.143.138:8082', '180.94.64.114:8080', '62.68.43.114:8080',
            '190.122.186.221:8080', '41.65.168.58:8080', '197.59.121.139:8080', '121.183.203.76:3128',
            '168.131.152.107:3128', '210.179.122.39:3128', '210.103.3.169:8080', '45.242.95.246:8080',
            '197.44.150.67:80', '197.54.4.204:8080', '134.35.254.46:8080', '217.174.150.8:8080', '185.28.249.109:8080',
            '109.74.38.234:8080', '18.228.254.92:8080', '177.185.159.38:8080', '72.252.4.250:8080',
            '209.91.216.167:8080', '24.139.185.163:3128', '181.65.146.213:999', '74.85.156.94:8080',
            '109.74.35.186:8080', '186.232.252.196:8080', '134.35.186.216:8080', '134.35.132.125:8080',
            '89.109.64.190:8080', '94.155.119.10:3128', '200.4.218.108:8080', '41.79.60.14:8080', '195.8.51.55:8080',
            '185.121.2.31:8080', '187.125.23.26:8080', '118.163.83.21:3128', '200.115.53.225:3128',
            '43.240.112.243:8080', '167.172.138.162:8080', '118.167.179.141:8080', '91.144.20.192:8080',
            '185.189.151.80:3128', '46.246.40.234:3128', '185.128.37.4:8080', '27.111.42.145:8080',
            '121.52.138.168:8080', '185.145.144.14:8080', '89.134.183.73:8080', '103.81.77.65:83',
            '103.84.129.213:8080', '103.233.152.66:8080', '139.255.74.125:8080', '115.85.65.94:8080',
            '178.134.178.134:3128', '202.128.22.29:48678', '62.68.43.67:8080', '161.132.103.138:8080',
            '200.54.22.74:8080', '154.113.69.230:8080', '160.119.126.54:8080', '200.54.70.245:80',
            '154.113.69.154:8080', '197.149.128.25:8080', '165.227.42.211:8080', '64.225.31.63:1080',
            '200.85.167.102:8080', '165.98.139.26:8080', '114.249.115.168:9000', '103.204.220.18:82',
            '202.166.207.195:8080', '190.171.170.66:8080', '164.77.134.13:8080', '195.134.169.22:8080',
            '139.5.71.126:23500', '139.5.71.80:23500', '103.235.199.93:35947', '103.28.86.241:61954',
            '188.166.23.52:8118', '178.62.238.61:8118', '178.62.246.180:3128', '114.134.172.50:60664',
            '190.53.38.98:42925', '169.255.126.211:60546', '103.81.114.182:53281', '37.111.42.210:8080',
            '41.223.155.118:53281', '41.60.236.234:6833', '197.231.186.148:44728', '131.196.141.147:33729',
            '92.114.234.206:46685', '188.240.112.127:9090', '93.116.185.57:36471', '103.242.44.80:8080',
            '202.179.21.49:23500', '202.179.7.158:23500', '202.131.234.142:51702', '154.118.52.242:51667',
            '85.15.200.145:32108', '190.149.212.170:58043', '188.6.164.138:55042', '103.79.35.165:39338',
            '13.233.182.129:80', '103.250.166.4:6666', '196.20.107.60:80', '91.187.75.48:42296', '200.63.34.193:54371',
            '190.14.156.196:23500', '197.216.2.18:8080', '197.216.2.14:8080', '197.216.2.85:8080', '134.19.254.2:21231',
            '178.128.187.206:8118', '41.139.9.47:8080', '178.134.71.138:35942', '51.77.152.26:80', '94.130.179.24:8006',
            '46.162.193.21:34771', '185.44.229.227:34930', '190.214.9.10:41572', '92.222.82.77:80',
            '188.129.161.55:45437', '61.5.192.14:50884', '51.68.90.232:9090', '94.130.179.24:8046',
            '94.130.179.24:8010', '94.130.179.24:8032', '186.125.59.8:44363', '129.205.201.239:8080',
            '185.69.28.213:8080', '42.113.53.25:8080', '91.187.117.230:8087', '41.223.143.78:3128', '134.0.63.134:8000',
            '185.138.114.75:8080', '34.255.86.98:8080', '89.204.214.142:8080', '95.179.162.13:3128', '45.4.85.152:999',
            '39.109.123.188:3128', '178.128.62.70:8080', '196.175.251.102:8080', '182.161.38.50:3128',
            '47.91.234.3:3128', '197.221.89.70:8080', '190.5.118.42:8080', '95.179.162.13:8080', '45.5.119.46:999',
            '160.119.128.122:8080', '178.128.22.144:8888', '102.176.160.109:8080', '178.128.223.132:8080',
            '190.80.11.32:8080', '200.4.161.83:3128', '190.109.199.6:8080', '196.175.251.102:80', '91.137.140.89:8082',
            '46.209.131.245:8080', '5.160.150.152:8080', '185.72.27.12:8080', '5.160.150.83:8080',
            '185.20.198.108:8080', '62.201.238.250:8080', '62.201.228.138:8080', '41.63.170.142:8080',
            '149.255.154.62:8080', '167.86.92.144:3128', '203.45.16.197:8080', '154.0.155.205:8080',
            '27.113.241.87:8080', '81.162.243.249:8080', '41.210.161.114:80', '88.255.217.164:8080',
            '185.136.243.189:8080', '176.235.99.114:30865', '172.80.253.50:3128', '191.97.72.128:999',
            '88.250.65.219:8080', '91.93.73.229:7070', '193.95.106.249:3128', '118.174.211.220:11', '61.7.171.252:8080',
            '180.180.123.40:80', '46.246.6.2:3128', '185.194.25.77:8080', '181.188.166.74:8080', '186.94.182.188:8080',
            '190.202.24.66:3128', '128.199.241.140:8080', '128.199.72.10:1080', '181.188.166.82:8080',
            '128.199.191.84:3128', '159.65.128.217:8989', '167.99.74.77:8000', '82.75.238.164:8888',
            '167.179.4.134:8080', '159.203.44.177:3128', '125.209.115.186:8080', '191.97.9.189:999',
            '191.97.14.100:999', '190.93.176.70:8080', '190.128.225.14:3128', '190.104.142.78:8080',
            '190.128.203.214:3128', '143.255.142.80:8080', '190.42.189.28:8080', '191.97.2.50:999',
            '185.132.251.128:8080', '138.197.150.145:3128', '110.39.174.57:8080', '182.176.164.41:8080',
            '202.142.155.250:8080', '110.37.216.118:8080', '213.6.162.6:8080', '213.6.28.65:8080', '41.204.87.90:8080',
            '190.61.63.217:999', '103.101.17.170:8080', '203.81.75.37:8080', '79.110.40.81:8080', '190.107.5.51:3128',
            '45.117.237.158:8080', '77.237.121.22:8080', '60.53.199.121:8080', '113.23.138.231:8989',
            '212.92.204.54:8080', '77.237.121.19:8080', '154.66.125.18:8080', '41.207.54.154:443', '165.16.58.1:8080',
            '165.16.109.50:8080', '93.99.176.84:3128', '194.213.217.254:8080', '85.206.128.79:80', '104.244.75.26:8080',
            '89.29.100.212:3128', '104.244.77.254:8080', '154.118.128.106:8080', '212.92.204.54:80',
            '197.157.255.38:8080', '180.149.96.133:8080', '190.61.44.90:999', '43.250.127.98:9001',
            '190.217.104.227:999', '190.248.153.162:8080', '132.255.21.58:999', '203.81.95.42:8080',
            '93.115.138.250:8080', '217.19.209.253:8080', '41.60.237.208:8080', '186.15.49.12:8080',
            '189.203.8.180:3128', '200.188.151.212:8080', '170.81.140.126:8080', '81.174.11.227:32393',
            '185.25.206.192:8080', '185.172.201.17:41258', '61.118.35.94:55725', '82.200.233.4:3128',
            '188.0.138.147:8080', '195.189.71.187:54767', '89.40.48.186:8080', '37.228.65.107:32052',
            '81.198.119.241:50835', '41.169.11.210:45088', '106.104.12.236:80', '123.195.152.139:32287',
            '154.73.65.90:45691', '182.52.90.42:51657', '78.188.65.105:49743', '185.51.36.152:41258',
            '154.72.197.106:48302', '82.117.244.85:31280', '193.34.93.221:53805', '220.135.165.38:8080',
            '77.58.96.177:80', '92.33.17.248:8080', '102.164.202.80:34934', '165.255.97.54:53281',
            '197.242.206.105:42386', '197.245.230.122:43943', '185.39.71.197:47983', '185.35.142.70:35432',
            '81.236.13.23:32500', '213.160.165.18:8081', '87.197.156.62:23500', '217.148.216.46:3128',
            '91.203.176.204:8080', '185.85.219.74:61068', '2.83.98.160:80', '92.86.10.42:42658', '89.34.208.223:33356',
            '89.42.133.58:8080', '92.84.56.10:49556', '5.2.164.205:52592', '46.102.73.244:53281',
            '195.182.152.238:38178', '80.255.91.38:32949', '77.38.21.239:8080', '37.252.67.184:50616',
            '85.236.234.163:8080', '213.154.0.120:53281', '154.66.245.47:46611', '94.230.149.73:47155',
            '103.3.225.114:52606', '81.200.63.108:60579', '31.209.110.159:31019', '31.209.96.50:57482',
            '163.53.182.148:50713', '37.17.38.196:53281', '154.127.32.105:35432', '41.85.189.66:57797',
            '95.168.96.42:34273', '154.127.32.89:60020', '190.211.115.66:30518', '217.196.81.221:37564',
            '85.238.167.170:38358', '178.213.130.159:60253', '95.216.88.76:44630', '176.67.80.160:8118',
            '196.188.73.56:3128', '109.75.47.248:37926', '35.200.179.207:8118', '190.53.46.14:38525',
            '190.53.46.50:40573', '35.194.149.184:1080', '14.201.234.2:50677', '58.96.148.97:8080',
            '190.214.52.226:53281', '150.242.35.148:53281', '181.196.151.82:50195', '103.112.39.206:50135',
            '200.105.179.186:30477', '201.204.168.106:80', '190.186.1.46:35144', '190.151.94.3:46615',
            '170.247.203.48:48263', '74.15.191.160:41564', '92.247.142.14:53281', '193.68.200.85:52825',
            '77.70.35.87:60186', '142.93.147.192:8118', '197.159.23.174:39150', '41.211.126.224:61255',
            '186.94.83.251:8080', '196.216.220.196:8080', '160.19.155.51:8080', '190.124.31.173:8080',
            '213.230.110.100:3128', '164.73.191.2:8080', '80.87.213.45:8080', '91.135.242.10:8080', '63.245.119.131:80',
            '203.202.248.35:80', '140.82.59.209:8080', '203.112.76.193:8080', '24.107.253.88:3128',
            '116.206.47.54:8080', '103.213.236.11:83', '108.160.129.126:3128', '134.17.133.238:8080',
            '196.223.137.207:8080', '80.94.229.172:3128', '154.127.161.28:8080', '181.177.140.123:8080',
            '148.255.76.55:999', '118.27.3.218:3128', '52.140.242.103:3128', '51.81.96.7:80', '94.237.2.104:8080',
            '89.219.21.174:8080', '41.220.114.154:8080', '84.52.56.248:8080', '41.33.179.195:8080',
            '187.162.11.94:3128', '187.188.190.217:999', '92.114.157.242:1080', '169.239.92.81:8080',
            '183.87.153.98:49602', '117.102.81.4:53281', '95.38.198.54:23500', '46.209.63.178:3128',
            '185.138.123.78:56588', '94.21.118.140:48322', '77.221.52.77:33694', '186.151.202.36:50109',
            '160.119.128.202:8080', '102.176.160.75:41701', '45.7.238.250:30980', '200.107.236.19:3128',
            '190.6.200.158:38256', '47.52.36.33:80', '159.138.1.185:80', '47.52.231.140:8080', '89.111.33.164:3128',
            '82.166.105.66:44081', '192.117.146.110:80', '41.84.156.46:8888', '154.79.245.30:37415', '61.75.77.182:80',
            '212.42.113.96:3128', '91.205.51.27:40108', '212.42.113.240:51715', '77.38.220.239:8080',
            '62.205.225.25:8080', '195.123.212.199:44394', '154.79.246.178:34577', '41.60.235.113:8080',
            '103.6.104.105:38898', '122.54.227.188:8080', '180.232.77.107:61965', '80.51.31.201:8080',
            '46.20.59.243:47497', '46.232.132.249:53769', '193.59.27.71:36748', '213.58.202.70:54214',
            '181.40.84.38:49674', '190.5.225.178:53570', '191.98.198.42:56633', '185.89.0.205:34927',
            '185.89.0.22:34927', '193.213.89.72:51024', '185.89.0.41:34927', '119.63.132.90:30759',
            '213.6.146.66:33746', '213.6.227.38:54796', '213.6.38.50:46812', '200.46.129.114:39592', '148.63.59.162:80',
            '185.37.211.222:50330', '5.135.108.117:3128', '212.57.43.16:50125', '109.122.80.234:44556',
            '41.203.240.50:3128', '128.199.233.132:44344', '5.22.154.106:37555', '158.255.249.58:38914',
            '91.230.44.133:3128', '185.157.161.11:8118', '185.157.161.85:8118', '92.113.28.24:53281',
            '195.214.222.75:8080', '109.87.46.125:51728', '186.167.33.244:42550', '190.207.37.233:3128',
            '42.116.18.172:54444', '117.2.17.26:53281', '62.4.54.158:53102', '41.215.180.237:54265',
            '155.0.181.254:31359', '197.211.245.50:53281', '197.211.238.220:54675', '213.230.68.184:3128',
            '81.95.230.211:3128', '179.27.83.222:47819', '94.205.140.158:34561', '185.132.176.250:8118',
            '185.10.166.130:8080', '91.194.42.51:80', '193.117.138.126:39900', '167.172.188.118:3128',
            '159.65.82.46:8118', '162.248.247.153:32592', '3.124.80.57:80', '41.190.33.162:8080', '193.95.228.13:53281',
            '41.58.162.46:34794', '202.57.47.122:36259', '196.2.14.250:51929', '116.212.129.58:39429',
            '96.9.73.80:56891', '119.15.82.222:37790', '103.9.188.229:36984', '96.9.69.164:53281',
            '106.104.151.142:58198', '191.241.166.249:41288', '201.204.168.106:63141', '186.15.233.218:45999',
            '201.204.46.10:39371', '169.255.75.117:49286', '185.50.56.230:32231', '190.7.141.66:56247',
            '163.204.247.97:9999', '39.137.69.7:8080', '117.88.176.135:3000', '183.166.162.104:9999',
            '118.113.245.171:9999', '109.175.29.2:57980', '185.16.13.160:47989', '154.73.85.1:43388',
            '200.54.194.13:53281', '175.100.30.156:25', '46.49.121.187:52101', '94.130.179.24:8015',
            '41.78.243.189:53281', '46.19.225.141:8888', '190.166.249.44:37359', '41.78.243.194:53281']
    pro = ['89.252.12.88:80']

    url1 = {'BTC/USD':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USD&limit=3&interval=1e-8'}
    url2 = {'USDT/USD':'https://api.hotbit.io/api/v1/order.depth?market=USDT/USD&limit=3&interval=1e-8'}
    url3 = {'ETH/USD':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USD&limit=3&interval=1e-8'}
    url4 = {'ETH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=ETH/BTC&limit=3&interval=1e-8'}
    url5 = {'LTC/BTC':'https://api.hotbit.io/api/v1/order.depth?market=LTC/BTC&limit=3&interval=1e-8'}
    url6 = {'BTC/USDT':'https://api.hotbit.io/api/v1/order.depth?market=BTC/USDT&limit=3&interval=1e-8'}
    url7 = {'ETH/USDT':'https://api.hotbit.io/api/v1/order.depth?market=ETH/USDT&limit=3&interval=1e-8'}
    url8 = {'XRP/BTC':'https://api.hotbit.io/api/v1/order.depth?market=XRP/BTC&limit=3&interval=1e-8'}
    url9 = {'ETH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=ETH/BTC&limit=3&interval=1e-8'}
    url10 = {'BCH/BTC':'https://api.hotbit.io/api/v1/order.depth?market=BCH/BTC&limit=3&interval=1e-8'}



    urls = [url1,
            # url2, url3,
            # url4, url5, url6,url7,url8,url9,url10
            ]
    hot = {}

    def set_proxy(session, proxy_candidates=pro, verify=False):
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
        str2hash = 'api_key={}&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","XLM"]&secret_key={}'.format(input1, input2)
        result = hashlib.md5(str2hash.encode())

        sign = result.hexdigest().upper()

        url = 'https://api.hotbit.io/api/v1/balance.query?api_key={}&assets=["BTC","ETH","ZEC","USDT","LTC","XRP","XLM"]&sign={}'.format(input1,
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
    print(loadRSS())
    print('HOT start TIME : ',(time.process_time() - start))