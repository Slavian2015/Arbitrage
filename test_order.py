import dash_html_components as html
import dash_design_kit as ddk
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)



def order_card():

    card = [html.Div(
                  id={
                  'type': 'show_test_order',
                  'index': '1'
                      }),
           html.Div(
                  id={
                      'type': 'show_test_order',
                      'index': '2'
                  }),
           html.Div(
                  id={
                      'type': 'show_test_order',
                      'index': '3'
                  }),
            ddk.Card(width=100,
                    children=[

                        ddk.Block(width=10,
                                  children="ALFA"),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="сколько",
                                          id={
                                              'type': 'tamount',
                                              'index': '1'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})
                                  ),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="Цена",
                                          id={
                                              'type': 'tprice',
                                              'index': '1'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})),

                        ddk.Block(width=20,
                                  children=html.Button('BUY',
                                               id={
                                                   'type': 'tbuy_btn',
                                                   'index': '1'
                                               },
                                               style={'text-align': 'center', 'max-width': '100px',
                                                      "background-color": "palegreen",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0)),
                        ddk.Block(width=30,
                                  children=html.Button('SELL',
                                               id={
                                                   'type': 'tsell_btn',
                                                   'index': '1'
                                               },
                                               style={'text-align': 'center', 'max-width': '120px',
                                                      "background-color": "tomato",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0,))

                    ]),
            ddk.Card(width=100,
                     children=[

                        ddk.Block(width=10,
                                  children="Live"),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="сколько",
                                          id={
                                              'type': 'tamount',
                                              'index': '2'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})
                                  ),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="Цена",
                                          id={
                                              'type': 'tprice',
                                              'index': '2'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})),

                        ddk.Block(width=20,
                                  children=html.Button('BUY',
                                               id={
                                                   'type': 'tbuy_btn',
                                                   'index': '2'
                                               },
                                               style={'text-align': 'center', 'max-width': '100px',
                                                      "background-color": "palegreen",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0)),
                        ddk.Block(width=30,
                                  children=html.Button('SELL',
                                               id={
                                                   'type': 'tsell_btn',
                                                   'index': '2'
                                               },
                                               style={'text-align': 'center', 'max-width': '120px',
                                                      "background-color": "tomato",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0,))

                    ]),
            ddk.Card(width=100,
                     children=[

                        ddk.Block(width=10,
                                  children="HOT"),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="сколько",
                                          id={
                                              'type': 'tamount',
                                              'index': '3'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})
                                  ),
                        ddk.Block(width=20,
                                  children=dcc.Input(
                                          placeholder="Цена",
                                          id={
                                              'type': 'tprice',
                                              'index': '3'
                                          },
                                          style={
                                              'border': 'double',
                                              'margin': '0',
                                              'background-color': 'ivory',
                                              'width': '-webkit-fill-available'})),

                        ddk.Block(width=20,
                                  children=html.Button('BUY',
                                               id={
                                                   'type': 'tbuy_btn',
                                                   'index': '3'
                                               },
                                               style={'text-align': 'center', 'max-width': '100px',
                                                      "background-color": "palegreen",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0)),
                        ddk.Block(width=30,
                                  children=html.Button('SELL',
                                               id={
                                                   'type': 'tsell_btn',
                                                   'index': '3'
                                               },
                                               style={'text-align': 'center', 'max-width': '120px',
                                                      "background-color": "tomato",
                                                      "border-radius": "20px",
                                                      'font-size': '15px'},
                                               n_clicks=0,))

                    ]),

            ]

    return card


# //{
# //    "1": {
# //        "key": "BtuWYH7DbtNLREeRUdfjfAxEiS71Lq6Wn2kyyoxS9zkiiVo2HtvZUg1CaMdJiuRHDUum9HutR",
# //        "api": "4Bmhw5cz4f5QzoXt8XbnEMwoapYFirS6ozkD11Q7RiuYg7DidgTdnJLf8MUU8Bb6YAL5D5m65uvBR4JTavip5uA6"
# //    },
# //    "2": {
# //        "key": "gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4",
# //        "api": "dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG"
# //    },
# //    "3": {
# //        "key": "7df7baa8-ae73-ddd1-2e8f6968ed3d5a89",
# //        "api": "37dfc47b7ef13b296f7011dad71a5775"
# //    },
# //    "4": {
# //        "key": "Chat id",
# //        "api": "Token"
# //    }
# //}