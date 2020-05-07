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
