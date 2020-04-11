import pandas as pd


# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)


alfa = {'BTC/USD': {'sell': [6791.122, 0.00058], 'buy': [6781.886, 0.03682]}, 'LTC/USD': {'sell': [41.2, 0.47692], 'buy': [41.16, 7.27098]}, 'ETH/USD': {'sell': [153.75, 0.7319055], 'buy': [153.5, 1.0121331]}, 'XRP/USD': {'sell': [0.18615, 38.82824326], 'buy': [0.185, 1.10438394]}, 'USD/USDT': {'sell': [0.998, 641.88], 'buy': [0.99, 204.0]}, 'BTC/USDT': {'sell': [6790.675, 0.012], 'buy': [6789.324, 0.0098]}, 'ETH/USDT': {'sell': [179.0, 0.05947], 'buy': [172.0, 5.859e-05]}, 'XRP/BTC': {'sell': [2.699e-05, 411.0], 'buy': [2.689e-05, 376.0]}, 'ETH/BTC': {'sell': [0.022632, 0.004], 'buy': [0.022603, 0.625]}, 'LTC/BTC': {'sell': [0.006067, 1.26], 'buy': [0.006055, 3.35]}, 'BCH/BTC': {'sell': [0.039, 0.001], 'buy': [0.03345002, 0.01913302]}, 'ZEC/BTC': {'sell': [0.006377, 0.48318062], 'buy': [0.004456, 2.7744614]}}


live = {'BTC/USD': {'sell': ['7100.1', '0.01333427'], 'buy': ['7.1E+3', '0.24016986']}, 'LTC/USD': {'sell': ['43.89', '2.43'], 'buy': ['43.5', '6.55440079']}, 'ETH/USD': {'sell': ['163.13104', '0.9346'], 'buy': ['162.32009', '0.24855688']}, 'XRP/USD': {'sell': ['0.19626', '56.57201913'], 'buy': ['0.19126', '29.9517467']}, 'USDT/USD': {'sell': ['1.03895', '1.55871615'], 'buy': ['1.02001', '2.44655256']}, 'BTC/USDT': {'sell': ['6917.53526304', '0.0107'], 'buy': ['6883', '0.24405520']}, 'ETH/USDT': {'sell': ['174', '0.01342255'], 'buy': ['142.00000154', '0.31528268']}, 'XRP/BTC': {'sell': ['0.00002718', '1281.8428'], 'buy': ['0.00002703', '65.64226718']}, 'ETH/BTC': {'sell': ['0.02293858', '5.97'], 'buy': ['0.02291118', '0.05117941']}, 'LTC/BTC': {'sell': ['0.006174', '5.43'], 'buy': ['0.00611575', '0.8']}, 'BCH/BTC': {'sell': ['0.0341', '3.2E-7'], 'buy': ['0.03392003', '0.00366808']}, 'ZEC/BTC': {'sell': ['0.00524318', '0.13801309'], 'buy': ['0.00521483', '0.05129181']}}


hot = {'BTC/USD': {'sell': ['7001.02', []], 'buy': ['6950.45', []]}, 'USDT/USD': {'sell': ['1.02', []], 'buy': ['1.0197', []]}, 'BTC/USDT': {'sell': ['6814.79', []], 'buy': ['6811.75', []]}, 'ETH/USDT': {'sell': ['155.58', []], 'buy': ['155.43', []]}, 'ETH/USD': {'sell': ['165.16', []], 'buy': ['161.91', []]}, 'LTC/BTC': {'sell': ['0.006103', []], 'buy': ['0.006086', []]}, 'XRP/BTC': {'sell': ['0.00002732', []], 'buy': ['0.00002712', []]}, 'BCH/BTC': {'sell': ['0.034374', []], 'buy': ['0.033699', []]}}



birgi = {'alfa': alfa, 'live': live, 'hot':hot}


birga = []
valin = []
valout = []
rates = []

def tab(item, value):
    for k,v in item.items():

        list = k.split('/')

        birga.append(value)
        valin.append(list[0])
        valout.append(list[1])

        r = ("{0:,.10f}".format(float((item[k]['buy'][0]))))
        r2 = r.replace(',','')
        rates.append(r2)


        birga.append(value)
        valin.append(list[1])
        valout.append(list[0])

        t = ("{0:,.10f}".format(float((item[k]['sell'][0]))))
        t2 = t.replace(',', '')
        rates.append(t2)

    return


for value, item in birgi.items():
    tab(item,value)


dw = {'birga': birga, 'valin': valin, 'valout': valout, 'rates': rates}
df = pd.DataFrame(data=dw)



dfs = pd.merge(df, df, left_on=df['valin'], right_on=df['valout'], how='outer')
dfs2 = pd.merge(df, df, left_on=df['valout'], right_on=df['valin'], how='outer')

# print(dfs.dtypes)
# dfs['rates_x'] = dfs['rates_x'].apply(pd.to_numeric, errors='coerce')
# dfs['rates_y'] = dfs['rates_y'].apply(pd.to_numeric, errors='coerce')
#
# dfs['PROFIT'] = dfs['rates_y'] - dfs['rates_x']
# dfs['PROFIT'] = dfs['PROFIT'].apply(pd.to_numeric, errors='coerce')

# print(dfs2.dtypes)
dfs2['rates_x'] = dfs2['rates_x'].apply(pd.to_numeric, errors='coerce')
dfs2['rates_y'] = dfs2['rates_y'].apply(pd.to_numeric, errors='coerce')
# print(dfs2.dtypes)


dfs2['PROFIT'] = dfs2['rates_y'] - dfs2['rates_x']
dfs2['PROFIT'] = dfs2['PROFIT'].apply(pd.to_numeric, errors='coerce')

dfs2['PERCENT'] = dfs2['PROFIT'] / dfs2['rates_y'] * 100
dfs2.drop(['key_0'], axis = 1, inplace = True)


dfs2['PERCENT'] = dfs2['PERCENT'].map('{:,.2f}%'.format)
dfs2['PROFIT'] = dfs2['PROFIT'].map('{:,.2f}'.format)

dfs2['rates_y'] = dfs2['rates_y'].map('{:,.2f}'.format)
dfs2['rates_x'] = dfs2['rates_x'].map('{:,.2f}'.format)

# ttt = dfs['PROFIT'].idxmax()
# ddk = dfs.loc[[ttt]]


result = dfs2[(dfs2['valin_x'] == dfs2['valout_y'])]
usdt = dfs2[(dfs2['valin_x'] == 'USD') & (dfs2['valout_y'] == 'USDT')]
usd = dfs2[(dfs2['valin_x'] == 'USDT') & (dfs2['valout_y'] == 'USD')]


final = result.append([usdt, usd])


print(final)