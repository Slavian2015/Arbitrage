import os
import json
import requests
import pandas as pd

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)



main_path_data = os.path.abspath("./data")
# url = 'https://api.hotbit.io/api/v1/order.depth?market=BTC/USD&limit=3&interval=1e-8'
# # url = 'https://btc-alpha.com/api/v1/orderbook/BTC_USD'
# # # url = 'https://api.livecoin.net/exchange/all/order_book'
# res = requests.request("GET", url)
# exam = res.json()

dfs = pd.read_csv(main_path_data + "\\final.csv")
f = open(main_path_data + "\\regim.json")
regim = json.load(f)


################  20.04    ##################################

dfs['volume_x'] = dfs['volume_x'].apply(pd.to_numeric, errors='coerce')
dfs['volume_y'] = dfs['volume_y'].apply(pd.to_numeric, errors='coerce')
dfs["perc"] = dfs["perc"].str.replace("%", "").astype(float)

ids = pd.DataFrame()

for i in regim:

    if regim[i]["option"] == 'active':
        if not regim[i]["order"]:

            print("2")
            # dfs["perc"] = dfs["perc"].replace("%", "").astype(float)
            dfs["volume_x"] = dfs["volume_x"].astype(float)
            dfs["volume_y"] = dfs["volume_y"].astype(float)
            filterx = dfs[dfs["volume_x"] < dfs["volume_y"]].index
            dfs.loc[filterx, "volume"] = dfs.loc[filterx,"volume_x"] * float(regim[i]["per"]) / 100
            filtery = dfs[dfs["volume_x"] > dfs["volume_y"]].index
            dfs.loc[filtery, "volume"] = dfs.loc[filtery,"volume_x"] * float(regim[i]["per"]) / 100
            dfs["volume"] = dfs["volume"].astype(float)
            dft = dfs[(dfs["birga_x"] == regim[i]["birga1"]) &
                  (dfs["birga_y"] == regim[i]["birga2"]) &
                  (dfs["valin_x"] == regim[i]["val1"]) &
                  (dfs["valin_y"] == regim[i]["val2"]) &
                  (dfs["valout_y"] == regim[i]["val3"]) &
                  (dfs["perc"] > regim[i]["profit"])
                      # & (dfs["volume"] > float(regim[k]["order"]))
            ]
            ids = pd.concat([dft,ids], ignore_index=False, join='outer')

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
                      (dfs["volume"] > regim[i]["order"])]
            ids = pd.concat([dft, ids], ignore_index=False, join='outer')
    else:
        pass

print(ids)

################  20.04    ##################################


# def change():
#     a_file = open(main_path_data + "\\regim.json", "r")
#     json_object = json.load(a_file)
#     a_file.close()
#     print(json_object)
#
#
#     index ='1'
#
#     json_object[index]['option'] = "active"
#     json_object[index]['val1'] = val1
#     json_object[index]['val1'] = val1
#     json_object[index]['val1'] = val1
#     json_object[index]['birga1'] = birga1
#     json_object[index]['birga2'] = birga2
#     json_object[index]['profit'] = profit
#     json_object[index]['order'] = order
#     json_object[index]['per'] = per
#
#
#
#     a_file = open(main_path_data + "\\regim.json", "w")
#     json.dump(json_object, a_file)
#     a_file.close()

