import pandas as pd
import json
import numpy as np
import Hot_parser
import Live_parser
import A_parser
import os
import datetime as dt

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


# alfa = {'BTC/USD': {'sell': [7000.122, 0.00058], 'buy': [6781.886, 0.03682]}, 'LTC/USD': {'sell': [41.2, 0.47692], 'buy': [41.16, 7.27098]}, 'ETH/USD': {'sell': [153.75, 0.7319055], 'buy': [153.5, 1.0121331]}, 'XRP/USD': {'sell': [0.18615, 38.82824326], 'buy': [0.185, 1.10438394]}, 'USD/USDT': {'sell': [0.998, 641.88], 'buy': [0.99, 204.0]}, 'BTC/USDT': {'sell': [6790.675, 0.012], 'buy': [6789.324, 0.0098]}, 'ETH/USDT': {'sell': [179.0, 0.05947], 'buy': [172.0, 5.859e-05]}, 'XRP/BTC': {'sell': [2.699e-05, 411.0], 'buy': [2.689e-05, 376.0]}, 'ETH/BTC': {'sell': [0.022632, 0.004], 'buy': [0.022603, 0.625]}, 'LTC/BTC': {'sell': [0.006067, 1.26], 'buy': [0.006055, 3.35]}, 'BCH/BTC': {'sell': [0.039, 0.001], 'buy': [0.03345002, 0.01913302]}, 'ZEC/BTC': {'sell': [0.006377, 0.48318062], 'buy': [0.004456, 2.7744614]}}
# live = {'BTC/USD': {'sell': ['7115.99365', '0.0126934'], 'buy': ['7079.001', '0.0035635']}, 'LTC/USD': {'sell': ['42.47', '0.1'], 'buy': ['42.24', '1.84']}, 'ETH/USD': {'sell': ['164.14', '0.23099188'], 'buy': ['162.48974', '0.6528']}, 'XRP/USD': {'sell': ['0.19385', '7.66806089'], 'buy': ['0.18956', '364.64975524']}, 'USDT/USD': {'sell': ['1.04398', '21.11918813'], 'buy': ['1.02501', '36']}, 'BTC/USDT': {'sell': ['6.95E+3', '0.03181925'], 'buy': ['6859.04578501', '0.01']}, 'ETH/USDT': {'sell': ['170.99999999', '0.02112591'], 'buy': ['149.1', '0.00466711']}, 'XRP/BTC': {'sell': ['0.00002715', '67.77328'], 'buy': ['0.00002699', '10.8185632']}, 'ETH/BTC': {'sell': ['0.02320816', '0.01679207'], 'buy': ['0.023064', '5.97']}, 'LTC/BTC': {'sell': ['0.006035', '0.0174'], 'buy': ['0.00597483', '10.1366']}, 'BCH/BTC': {'sell': ['0.03299954', '0.03407698'], 'buy': ['0.03220001', '0.07028846']}, 'ZEC/BTC': {'sell': ['0.00521679', '0.17689186'], 'buy': ['0.00520734', '0.01450943']}}
# hot = {'BTC/USD': {'sell': [7009.46, 0.002446], 'buy': [6538.48, 0.003686]}, 'USDT/USD': {'sell': [1.0126, 0.01], 'buy': [1.0123, 569.79]}, 'ETH/USD': {'sell': [160.67, 0.000261], 'buy': [154.4, 0.001049]}, 'ETH/BTC': {'sell': [0.02321272, 2.5], 'buy': [0.02318881, 2.5]}, 'LTC/BTC': {'sell': [0.005996, 7.1374], 'buy': [0.005992, 11.2239]}, 'BTC/USDT': {'sell': [6930.99, 0.14], 'buy': [6930.73, 0.14]}, 'ETH/USDT': {'sell': [160.91, 2.8], 'buy': [160.89, 2e-05]}, 'XRP/BTC': {'sell': [2.729e-05, 923.1], 'buy': [2.704e-05, 2.1]}, 'BCH/BTC': {'sell': [0.032866, 0.3191], 'buy': [0.03222, 0.2939]}}

main_path_data = os.path.abspath("./data")

if os.path.isfile(main_path_data + "\\commis.json"):
    f = open(main_path_data + "\\commis.json")
    compp = json.load(f)
    pass
else:
    dictionary= {"main": {
        "hot": 1.0006,
        "alfa": 1.002,
        "live": 1.0018
                        }}

    compp = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(main_path_data + "\\commis.json", "w") as outfile:
        outfile.write(compp)
        outfile.close()

        pass


def restart():

    hot = Hot_parser.loadRSS()
    live = Live_parser.restart()
    alfa = A_parser.loadRSS()

    birgi = {'alfa': alfa, 'live': live, 'hot': hot}

    birga = []
    valin = []
    valout = []
    rates = []

    def tab(item, value):
        f = open(main_path_data + "\\commis.json")
        com = json.load(f)

        for k,v in item.items():
            list = k.split('/')

            birga.append(value)
            valin.append(list[0])
            valout.append(list[1])

            r = ("{0:,.10f}".format(float((item[k]['buy'][0]))))
            r2 = r.replace(',', '')
            rr = np.asarray(com['main'][value])

            # print('TYPE :', type(rr))
            r3 = (float(r2) / float(rr))
            rates.append(r2)

            birga.append(value)
            valin.append(list[1])
            valout.append(list[0])

            t = ("{0:,.10f}".format(float((item[k]['sell'][0]))))
            t2 = t.replace(',', '')

            t3 = float(t2) * float(com['main'][value])
            rates.append(t2)
            # if value == "live" or value == "hot":
            #     list = k.split('/')
            #
            #     birga.append(value)
            #     valin.append(list[0])
            #     valout.append(list[1])
            #
            #     r = ("{0:,.10f}".format(float((item[k]['buy'][0]))))
            #     r2 = r.replace(',','')
            #     rr = np.asarray(com['main'][value])
            #
            #     # print('TYPE :', type(rr))
            #     r3 = (float(r2) * float(rr))
            #     rates.append(r3)
            #
            #
            #     birga.append(value)
            #     valin.append(list[1])
            #     valout.append(list[0])
            #
            #     t = ("{0:,.10f}".format(float((item[k]['sell'][0]))))
            #     t2 = t.replace(',', '')
            #
            #     t3 = float(t2) * float(com['main'][value])
            #     rates.append(t3)
            # else:
            #     list = k.split('/')
            #
            #     birga.append(value)
            #     valin.append(list[0])
            #     valout.append(list[1])
            #
            #     r = ("{0:,.10f}".format(float((item[k]['sell'][0]))))
            #     r2 = r.replace(',', '')
            #     rr = np.asarray(com['main'][value])
            #
            #     # print('TYPE :', type(rr))
            #     r3 = (float(r2) * float(rr))
            #     rates.append(r3)
            #
            #     birga.append(value)
            #     valin.append(list[1])
            #     valout.append(list[0])
            #
            #     t = ("{0:,.10f}".format(float((item[k]['buy'][0]))))
            #     t2 = t.replace(',', '')
            #
            #     t3 = float(t2) * float(com['main'][value])
            #     rates.append(t3)

        return


    for value, item in birgi.items():
        tab(item,value)


    dw = {'birga': birga, 'valin': valin, 'valout': valout, 'rates': rates}
    df = pd.DataFrame(data=dw)

    dfs = pd.merge(df, df, left_on=df['valin'], right_on=df['valout'], how='outer')
    dfs2 = pd.merge(df, df, left_on=df['valout'], right_on=df['valin'], how='outer')

    # print(dfs.dtypes)
    dfs['rates_x'] = dfs['rates_x'].apply(pd.to_numeric, errors='coerce')
    dfs['rates_y'] = dfs['rates_y'].apply(pd.to_numeric, errors='coerce')

    dfs2['rates_x'] = dfs2['rates_x'].apply(pd.to_numeric, errors='coerce')
    dfs2['rates_y'] = dfs2['rates_y'].apply(pd.to_numeric, errors='coerce')
    # print(dfs2.dtypes)


    dfs2.drop(['key_0'], axis = 1, inplace = True)

    dfs2['rates_y'] = dfs2['rates_y'].map('{:,.10f}'.format)
    dfs2['rates_x'] = dfs2['rates_x'].map('{:,.10f}'.format)


    result = dfs2[(dfs2['valin_x'] == dfs2['valout_y'])]
    usdt = dfs2[(dfs2['valin_x'] == 'USD') & (dfs2['valout_y'] == 'USDT')]
    usd = dfs2[(dfs2['valin_x'] == 'USDT') & (dfs2['valout_y'] == 'USD')]


    final = result.append([usdt, usd])
    final.reset_index(inplace=True, drop = True)
    final.reset_index(level=0, inplace=True)
    filter = final[(final['birga_x'] == final['birga_y']) &
                   (final['rates_x'] < final['rates_y']) &
                   (final['valin_x'] == final['valout_y'])]


    final = final.drop(filter['index'], axis=0)

    var1 = final[final["valin_x"].isin(["USD", "USDT"])]
    var2 = final[final["valin_y"].isin(["USD", "USDT"])]
    var3 = final[(final["valin_x"] == "BTC") & (~final["valin_y"].isin(["USD", "USDT"]))]
    var4 = final[(final["valin_y"] == "BTC") & (~final["valin_x"].isin(["USD", "USDT"]))]

    var = {'var1': var1, 'var2': var2, 'var3': var3, 'var4': var4}

    def calc1(result):
        result['start'] = "100"
        result["start"] = result["start"].str.replace(",", "").astype(float)
        result["rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result["rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result['step'] = (result['start']) / (result['rates_x'])
        result['back'] = result['step'] * (result['rates_y'])
        result['profit'] = result['back'] - result['start']
        result['perc'] = (((result['profit']) / (result['start'])) * 100)
        return result
    def calc2(result):

        result['start'] = "100"
        result["start"] = result["start"].str.replace(",", "").astype(float)
        result["rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result["rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result['step'] = (result['start']) * (result['rates_x'])
        result['back'] = result['step'] / (result['rates_y'])
        result['profit'] = result['back'] - result['start']
        result['perc'] = (((result['profit']) / (result['start'])) * 100)

        return result


    dft = pd.DataFrame()
    for i, v in var.items():
        if v.shape[0] > 0:
            if i == 'var1' or i == 'var3':
                dft = dft.append(calc1(v))
            else:
                dft = dft.append(calc2(v))




    dft['rates_y'] = dft['rates_y'].map('{:,.5f}'.format)
    dft['rates_x'] = dft['rates_x'].map('{:,.5f}'.format)
    dft['step'] = dft['step'].map('{:,.5f}'.format)
    dft['back'] = dft['back'].map('{:,.5f}'.format)
    dft['profit'] = dft['profit'].map('{:,.5f}'.format)
    dft['perc'] = dft['perc'].map('{:,.2f}%'.format)



    # print(dft)









    now = dt.datetime.now()
    final.loc[:, 'TIME'] = now.strftime("%H:%M:%S")
    print("Restart :", '\n')
    # print(final)
    #
    # final.to_csv(main_path_data + "\\final.csv", index=False, header=True)

    return dft
final = restart()