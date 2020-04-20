import pandas as pd
import json
import numpy as np
import Hot_parser
import Live_parser
import A_parser
import os
import datetime as dt



# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', None)



# alfa = {'BTC/USD': {'sell': [7000.122, 0.00058], 'buy': [6781.886, 0.03682]}, 'LTC/USD': {'sell': [41.2, 0.47692], 'buy': [41.16, 7.27098]}, 'ETH/USD': {'sell': [153.75, 0.7319055], 'buy': [153.5, 1.0121331]}, 'XRP/USD': {'sell': [0.18615, 38.82824326], 'buy': [0.185, 1.10438394]}, 'USD/USDT': {'sell': [0.998, 641.88], 'buy': [0.99, 204.0]}, 'BTC/USDT': {'sell': [6790.675, 0.012], 'buy': [6789.324, 0.0098]}, 'ETH/USDT': {'sell': [179.0, 0.05947], 'buy': [172.0, 5.859e-05]}, 'XRP/BTC': {'sell': [2.699e-05, 411.0], 'buy': [2.689e-05, 376.0]}, 'ETH/BTC': {'sell': [0.022632, 0.004], 'buy': [0.022603, 0.625]}, 'LTC/BTC': {'sell': [0.006067, 1.26], 'buy': [0.006055, 3.35]}, 'BCH/BTC': {'sell': [0.039, 0.001], 'buy': [0.03345002, 0.01913302]}, 'ZEC/BTC': {'sell': [0.006377, 0.48318062], 'buy': [0.004456, 2.7744614]}}
# live = {'BTC/USD': {'sell': ['7115.99365', '0.0126934'], 'buy': ['7079.001', '0.0035635']}, 'LTC/USD': {'sell': ['42.47', '0.1'], 'buy': ['42.24', '1.84']}, 'ETH/USD': {'sell': ['164.14', '0.23099188'], 'buy': ['162.48974', '0.6528']}, 'XRP/USD': {'sell': ['0.19385', '7.66806089'], 'buy': ['0.18956', '364.64975524']}, 'USDT/USD': {'sell': ['1.04398', '21.11918813'], 'buy': ['1.02501', '36']}, 'BTC/USDT': {'sell': ['6.95E+3', '0.03181925'], 'buy': ['6859.04578501', '0.01']}, 'ETH/USDT': {'sell': ['170.99999999', '0.02112591'], 'buy': ['149.1', '0.00466711']}, 'XRP/BTC': {'sell': ['0.00002715', '67.77328'], 'buy': ['0.00002699', '10.8185632']}, 'ETH/BTC': {'sell': ['0.02320816', '0.01679207'], 'buy': ['0.023064', '5.97']}, 'LTC/BTC': {'sell': ['0.006035', '0.0174'], 'buy': ['0.00597483', '10.1366']}, 'BCH/BTC': {'sell': ['0.03299954', '0.03407698'], 'buy': ['0.03220001', '0.07028846']}, 'ZEC/BTC': {'sell': ['0.00521679', '0.17689186'], 'buy': ['0.00520734', '0.01450943']}}
# hot = {'BTC/USD': {'sell': [7009.46, 0.002446], 'buy': [6538.48, 0.003686]}, 'USDT/USD': {'sell': [1.0126, 0.01], 'buy': [1.0123, 569.79]}, 'ETH/USD': {'sell': [160.67, 0.000261], 'buy': [154.4, 0.001049]}, 'ETH/BTC': {'sell': [0.02321272, 2.5], 'buy': [0.02318881, 2.5]}, 'LTC/BTC': {'sell': [0.005996, 7.1374], 'buy': [0.005992, 11.2239]}, 'BTC/USDT': {'sell': [6930.99, 0.14], 'buy': [6930.73, 0.14]}, 'ETH/USDT': {'sell': [160.91, 2.8], 'buy': [160.89, 2e-05]}, 'XRP/BTC': {'sell': [2.729e-05, 923.1], 'buy': [2.704e-05, 2.1]}, 'BCH/BTC': {'sell': [0.032866, 0.3191], 'buy': [0.03222, 0.2939]}}

main_path_data = os.path.abspath("./data")

#################################   COMMISSIONS   ##########################################
if os.path.isfile(main_path_data + "\\commis.json"):
    f = open(main_path_data + "\\commis.json")
    com = json.load(f)
    pass
else:
    dictionary= {"main": {
        "hot": 1.0006,
        "alfa": 1.002,
        "live": 1.0018
                        }}
    com = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(main_path_data + "\\commis.json", "w") as outfile:
        outfile.write(com)
        outfile.close()
        pass



# def reg():
#
#     #################################      REGIMS      ##########################################
#
#     if os.path.isfile(main_path_data + "\\regim.json"):
#         pass
#     else:
#         dictionary = {"1": {"option": "off",
#                            "val1": "",
#                            "val2": "",
#                            "val3": "",
#                            "birga1": "",
#                            "birga2": "",
#                            "profit": "",
#                            "order": "",
#                             "per": ""
#                             }}
#         regim = json.dumps(dictionary, indent=4)
#
#         # Writing to sample.json
#         with open(main_path_data + "\\regim.json", "w") as outfile:
#             outfile.write(regim)
#             outfile.close()
#             pass
#
#     return
#
# reg()

def restart():

    hot = Hot_parser.loadRSS()
    live = Live_parser.restart()
    alfa = A_parser.loadRSS()

    birgi = {'alfa': alfa, 'live': live, 'hot': hot}

    birga = []
    valin = []
    valout = []
    rates = []
    volume = []

    def tab(item, value):

        for k, v in item.items():
            list = k.split('/')


            abc = [0, 1, 2]
            for i in abc:
                birga.append(value)
                valin.append(list[0])
                valout.append(list[1])


                r = ("{0:,.10f}".format(float((item[k]['buy'][i][0]))))
                r2 = r.replace(',', '')
                # r = item[k]['buy'][i][0]
                # r3 = r.replace(',', '')
                # r2 = ("{0:,.10f}".format(float((r3))))



                v = ("{0:,.10f}".format(float((item[k]['buy'][i][1]))))
                v2 = v.replace(',', '')
                # v = item[k]['buy'][i][1]
                # v3 = v.replace(',', '')
                # v2 = ("{0:,.10f}".format(float((v3))))




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

    # dfs = pd.merge(df, df, left_on=df['valin'], right_on=df['valout'], how='outer')
    dfs2 = pd.merge(df, df, left_on=df['valout'], right_on=df['valin'], how='outer')

    # print(dfs.dtypes)
    # dfs['rates_x'] = dfs['rates_x'].apply(pd.to_numeric, errors='coerce')
    # dfs['rates_y'] = dfs['rates_y'].apply(pd.to_numeric, errors='coerce')

    dfs2['rates_x'] = dfs2['rates_x'].apply(pd.to_numeric, errors='coerce')
    dfs2['rates_y'] = dfs2['rates_y'].apply(pd.to_numeric, errors='coerce')


    dfs2['volume_x'] = dfs2['volume_x'].apply(pd.to_numeric, errors='coerce')
    dfs2['volume_y'] = dfs2['volume_y'].apply(pd.to_numeric, errors='coerce')
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
        f = open(main_path_data + "\\commis.json")
        com = json.load(f)
        result.loc[:, 'start'] = "100"
        result.loc[:, "start"] = result["start"].str.replace(",", "").astype(float)
        result.loc[:, "rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result.loc[:, "rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result.loc[:, 'step'] = (result['start']) / ((result['rates_x'] * com['main'][result.iloc[0]['birga_x']]))
        result.loc[:, 'back'] = result['step'] * ((result['rates_y']) / com['main'][result.iloc[0]['birga_y']])
        result.loc[:, 'profit'] = result['back'] - result['start']
        result.loc[:, 'perc'] = (((result['profit']) / (result['start'])) * 100)
        f.close()
        return result
    def calc2(result):

        f = open(main_path_data + "\\commis.json")
        com = json.load(f)

        result.loc[:, 'start'] = "100"
        result.loc[:, "start"] = result["start"].str.replace(",", "").astype(float)
        result.loc[:, "rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result.loc[:, "rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result.loc[:, 'step'] = (result['start']) * ((result['rates_x'] / com['main'][result.iloc[0]['birga_x']]))
        result.loc[:, 'back'] = result['step'] / ((result['rates_y']) * com['main'][result.iloc[0]['birga_y']])
        result.loc[:, 'profit'] = result['back'] - result['start']
        result.loc[:, 'perc'] = (((result['profit']) / (result['start'])) * 100)
        f.close()
        return result


    dft = pd.DataFrame()
    for i, v in var.items():
        if v.shape[0] > 0:
            if i == 'var1' or i == 'var3':
                dft = dft.append(calc1(v))
            else:
                dft = dft.append(calc2(v))


    now = dt.datetime.now()
    dft.loc[:, 'TIME'] = now.strftime("%H:%M:%S")

    dft.drop(['index'], axis=1, inplace=True)

    dft = dft[['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y','valin_x','valin_y','valout_y','volume_x','volume_y','start','step','back','profit','perc']]

    print("Restart :", '\n')
    # print(final)

    dict = {'VALUTA': ["USD", "BTC", "ETH", "LTC"],
            'Alpha': [5000, 0.1, 50, 65],
            'Live': [5000, 0.1, 50, 65],
            'Hot': [5000, 0.1, 50, 65]}
    valuta = pd.DataFrame(dict)
    valuta["SUMMA"] = valuta["Alpha"] + valuta["Live"] + valuta["Hot"]
    dfs = dft

    def regim_filter():
        ids = pd.DataFrame()

        #################################      REGIMS      ##########################################

        if os.path.isfile(main_path_data + "\\regim.json"):
            f = open(main_path_data + "\\regim.json")
            regim = json.load(f)
            pass
        else:
            regim = {1: {"option": "off",
                                "val1": "",
                                "val2": "",
                                "val3": "",
                                "birga1": "",
                                "birga2": "",
                                "profit": "",
                                "order": "",
                                "per": ""}}
            ooo = json.dumps(regim, indent=4)
            # Writing to sample.json
            with open(main_path_data + "\\regim.json", "w") as outfile:
                outfile.write(ooo)
                outfile.close()
                pass


        dfs['volume_x'] = dfs['volume_x'].apply(pd.to_numeric, errors='coerce')
        dfs['volume_y'] = dfs['volume_y'].apply(pd.to_numeric, errors='coerce')
        # dfs["perc"] = dfs["perc"].str.replace("%", "").astype(float)
        dfs['volume_y'] = dfs['volume_y'].apply(pd.to_numeric, errors='coerce')
        # print(dfs["perc"])

        for i in regim:

            if regim[i]["option"] == 'active':
                if not regim[i]["order"]:
                    dfs["volume_x"] = dfs["volume_x"].astype(float)
                    dfs["volume_y"] = dfs["volume_y"].astype(float)
                    filterx = dfs[dfs["volume_x"] < dfs["volume_y"]].index
                    dfs.loc[filterx, "volume"] = dfs.loc[filterx, "volume_x"] * float(regim[i]["per"]) / 100
                    filtery = dfs[dfs["volume_x"] > dfs["volume_y"]].index
                    dfs.loc[filtery, "volume"] = dfs.loc[filtery, "volume_x"] * float(regim[i]["per"]) / 100
                    dfs["volume"] = dfs["volume"].astype(float)
                    dft = dfs[(dfs["birga_x"] == regim[i]["birga1"]) &
                              (dfs["birga_y"] == regim[i]["birga2"]) &
                              (dfs["valin_x"] == regim[i]["val1"]) &
                              (dfs["valin_y"] == regim[i]["val2"]) &
                              (dfs["valout_y"] == regim[i]["val3"]) &
                              (dfs["perc"] > regim[i]["profit"])
                              ]
                    ids = pd.concat([dft, ids], ignore_index=False, join='outer')

                else:


                    dfs["volume_x"] = dfs["volume_x"].astype(float)
                    dfs["volume_y"] = dfs["volume_y"].astype(float)
                    filterx = dfs[dfs["volume_x"] < dfs["volume_y"]].index
                    dfs.loc[filterx, "volume"] = dfs.loc[filterx, "volume_x"] / 2
                    filtery = dfs[dfs["volume_x"] > dfs["volume_y"]].index
                    dfs.loc[filtery, "volume"] = dfs.loc[filtery, "volume_x"] / 2
                    dfs["volume"] = dfs["volume"].astype(float)
                    dft = dfs[(dfs["birga_x"] == regim[i]["birga1"]) &
                              (dfs["birga_y"] == regim[i]["birga2"]) &
                              (dfs["valin_x"] == regim[i]["val1"]) &
                              (dfs["valin_y"] == regim[i]["val2"]) &
                              (dfs["valout_y"] == regim[i]["val3"]) &
                              (dfs["perc"] > regim[i]["profit"]) &
                              (dfs["volume"] > float(regim[i]["order"]))]
                    ids = pd.concat([dft, ids], ignore_index=False, join='outer')

            else:
                pass

        return ids

    fdf = regim_filter()

    # print("  FILTER df  :", '\n',  fdf)

    if fdf.shape[0] > 0:
        fdf['rates_y'] = fdf['rates_y'].map('{:,.2f}'.format)
        fdf['rates_x'] = fdf['rates_x'].map('{:,.2f}'.format)
        fdf['step'] = fdf['step'].map('{:,.2f}'.format)
        fdf['back'] = fdf['back'].map('{:,.2f}'.format)
        fdf['profit'] = fdf['profit'].map('{:,.2f}'.format)
        fdf['perc'] = fdf['perc'].map('{:,.2f}%'.format)
        fdf['volume_x'] = fdf['volume_x'].map('{:,.5f}'.format)
        fdf['volume_y'] = fdf['volume_y'].map('{:,.5f}'.format)
        fdf['volume'] = fdf['volume'].map('{:,.5f}'.format)
    else:
        pass

    print( "FDF   :",  fdf)

    return fdf, valuta
fin = restart()
final = fin[0]
valuta = fin[1]

