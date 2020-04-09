import time
import os.path
import pandas
import pandas as pd
import os
import csv
import datetime as dt
from dash import Dash, callback_context, no_update
from dash.dependencies import Input, Output, State
from dash_table import DataTable

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


alfa = {
    "USDBTC": {
        "ask": [["7400"],["7395"],["7390"]],
        "bid": [["7401"],["7405"],["7410"]],
    }
}

live = {
    "USDBTC": {
        "ask": [["7420"],["7395"],["7390"]],
        "bid": [["7430"],["7435"],["7440"]],
    }
}

hot = {
    "USDBTC": {
        "ask": [["7500"],["7495"],["7400"]],
        "bid": [["7410"],["7415"],["7460"]],
    }
}


birgi = {'alfa': alfa, 'live': live, 'hot':hot}


birga = []
valin = []
valout = []
rates = []

def tab(item, value):
    for k,v in item.items():

        birga.append(value)
        valin.append(k[:3])
        valout.append(k[-3:])
        rates.append(item[k]['bid'][0][0])

        birga.append(value)
        valin.append(k[-3:])
        valout.append(k[:3])
        rates.append(item[k]['ask'][0][0])
    return

for value, item in birgi.items():
    tab(item,value)


dw = {'birga': birga, 'valin': valin, 'valout': valout, 'rates': rates}
df = pd.DataFrame(data=dw)
dfs = pd.merge(df, df, left_on=df['valin'], right_on=df['valout'], how='outer')
dfs['rates_x'] = dfs['rates_x'].astype(float)
dfs['rates_y'] = dfs['rates_y'].astype(float)
dfs['PROFIT'] = dfs['rates_y'] - dfs['rates_x']


ttt = dfs['PROFIT'].idxmax()
ddk = dfs.loc[[ttt]]


print(ddk)
