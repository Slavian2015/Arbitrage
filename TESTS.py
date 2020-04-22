# import os
# import json
# import requests
# import pandas as pd
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# import dash_design_kit as ddk
# import uuid
# import dash_table
# from app import dash_app
# from VILKA import valuta

#
# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', None)

dictionary = {'1':
                              {"key": '',
                                "api": ''},
                          '2':
                              {"key": '',
                               "api": ''},
                          '3':
                              {"key": '',
                               "api": ''},
                          '4':
                              {"key": '',
                               "api": ''}
                          }


print('BEFORE :', dictionary)

dictionary['1']['key'] = "222"



print('AFTER :', dictionary)