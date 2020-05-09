import dash_html_components as html
import dash_design_kit as ddk
import pandas as pd
import dash_bootstrap_components as dbc


##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)



def film_start():
    rows = []
    rows.append(html.Tr([html.Td("№", style={'text-align': 'center'}),
                         html.Td("БИРЖА", style={'text-align': 'center'}),
                        html.Td("НАПРАВЛЕНИЕ", style={'text-align': 'center'}),
                        html.Td("ПРОФИТ", style={'text-align': 'center'}),
                        html.Td("Дейстиве", style={'text-align': 'center'}),
                         html.Td("Результат", style={'text-align': 'center'})]))

    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_body,
                      bordered=True,
                      dark=True,
                      hover=True,
                      responsive=True,
                      striped=True,
                      style={'width':"100%"})



    return table


def film_list(db):
    all_cardsBD = db
    all_cardsBD.index += 1
    all_cardsBD['start'] = all_cardsBD['start'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['volume'] = all_cardsBD['volume'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['back'] = all_cardsBD['back'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['step'] = all_cardsBD['step'].apply(pd.to_numeric, errors='coerce')


    rows = []
    rows.append(html.Tr([html.Td("№", style={'text-align': 'center'}),
                         html.Td("БИРЖА", style={'text-align': 'center'}),
                        html.Td("НАПРАВЛЕНИЕ", style={'text-align': 'center'}),
                        html.Td("ПРОФИТ", style={'text-align': 'center'}),
                        html.Td("Дейстиве", style={'text-align': 'center'}),
                         html.Td("Результат", style={'text-align': 'center'})]))


    USD_fil = all_cardsBD[(all_cardsBD['valin_x'] == "USD") | (all_cardsBD['valin_x'] == "USDT")]
    BTC_fil = all_cardsBD[(all_cardsBD['valin_x'] == "BTC") & (all_cardsBD['valin_y'].isin(["USD", "USDT"]))]
    BTC_fil_main = all_cardsBD[(all_cardsBD['valin_x'] == "BTC") & (~all_cardsBD['valin_y'].isin(["USD", "USDT"]))]
    BTC_fil_main2 = all_cardsBD[(all_cardsBD['valin_y'] == "BTC") & (~all_cardsBD['valin_x'].isin(["USD", "USDT"]))]


    # print('###########    USD_fil  :', '\n',USD_fil)
    # print('###########    BTC_fil  :', '\n',BTC_fil)
    # print('###########    BTC_fil_main  :', '\n',BTC_fil_main)
    # print('###########    BTC_fil_main2  :', '\n',BTC_fil_main2)



    if USD_fil.shape[0]>0:
        for ind in USD_fil.index:
            rate1 = (USD_fil['start'][ind] / USD_fil['step'][ind])
            rate2 = (USD_fil['back'][ind] / USD_fil['step'][ind])
            step = (USD_fil['volume'][ind] * rate1)
            step2 = (rate2 * USD_fil['volume'][ind])
            rows.append(html.Tr([
                html.Td(style={'text-align': 'center'},
                        children=[ddk.Block(USD_fil['TIME'][ind]),
                                  ddk.Block(USD_fil['timer'][ind]),
                                  ddk.Block(id={'type': "uregim",'index': ind},
                                            children=USD_fil['regim'][ind])]),

                html.Td([
                    html.Tr(USD_fil['birga_x'][ind],
                            id={'type': "ubirga_1", 'index': ind}),
                    html.Tr(USD_fil['birga_y'][ind],
                            id={'type': "ubirga_2", 'index': ind})

                ]),

                html.Td(style={'padding': '0'},
                        children=[
                            html.Tr(html.Td(style={'padding': '0'},
                                            children=
                                            ddk.Block(width=100,
                                                      style={'width': '600px'},
                                                      children=[
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(step, style={"font-weight": "700"},
                                                                                        id={'type': "uval1_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(USD_fil['valin_x'][ind],
                                                                                        id={'type': "uval1",
                                                                                            'index': ind})]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(USD_fil['rates_x'][ind],
                                                                                        style={'text-align': 'center'},
                                                                                        id={'type':"urate1", 'index':ind}),
                                                                              ddk.Block("-->>")]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(USD_fil['volume'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval2_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(USD_fil['valin_y'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval2",
                                                                                            'index': ind})]),
                                                      ]))),

                            html.Tr(html.Td(style={'padding': '0'},
                                            children=
                                            ddk.Block(width=100,
                                                      style={'width': '600px'},
                                                      children=[
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(USD_fil['volume'][ind],
                                                                                        id={'type': "uval3_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(USD_fil['valin_y'][ind],
                                                                                        id={'type': "uval3",
                                                                                            'index': ind})]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(USD_fil['rates_y'][ind],
                                                                                        style={'text-align': 'center'},
                                                                                        id={'type':"urate2", 'index':ind} ),
                                                                              ddk.Block("-->>")]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(step2, style={"font-weight": "700",
                                                                                                      "text-align": "right"},
                                                                                        id={'type': "uval4_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(USD_fil['valout_y'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval4",
                                                                                            'index': ind})]),
                                                      ])
                                            ))]),

                html.Td([
                    html.Tr(USD_fil['perc'][ind], style={"font-weight": "700"})
                ]),

                html.Td([
                    html.Tr(
                        style={'text-align': 'center'},
                        children=[html.Button("Go !",
                                              style={'text-align': 'center', 'max-width': '100px',
                                                     "background-color": "palegreen",
                                                     "border-radius": "20px",
                                                     'font-size': '15px'},
                                              n_clicks=0,
                                              id={'type': "uorder_btn", 'index': ind})])
                ]),

                html.Td([html.Tr([], id={'type': "uorder_result", 'index': ind})])

            ]))
    else:
        pass

    if BTC_fil.shape[0] > 0:
        for ind in BTC_fil.index:
            rate1 = (BTC_fil['step'][ind] / BTC_fil['start'][ind])
            rate2 = (BTC_fil['step'][ind] / BTC_fil['back'][ind])
            step = (BTC_fil['volume'][ind] * rate1)
            step2 =(step / rate2)
            rows.append(html.Tr([
                html.Td(style={'text-align': 'center'}, children=[ddk.Block(BTC_fil['TIME'][ind]),
                                                                  ddk.Block(BTC_fil['timer'][ind]),
                                  ddk.Block(id={'type': "uregim",'index': ind},
                                            children=BTC_fil['regim'][ind])]),
                html.Td([
                    html.Tr(BTC_fil['birga_x'][ind],
                                    id={'type':"ubirga_1", 'index':ind}),
                    html.Tr(BTC_fil['birga_y'][ind],
                                    id={'type':"ubirga_2", 'index':ind})

                ]),   # Birga
                html.Td(style={'padding': '0'}, children=[
                    html.Tr(html.Td(style={'padding': '0'},
                                    children=
                                    ddk.Block(width=100,
                                              style={'width': '600px'},
                                              children=[
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(BTC_fil['volume'][ind],
                                                                                style={"font-weight": "700"},
                                                                                id={'type':"uval1_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil['valin_x'][ind],
                                                                                id={'type':"uval1", 'index':ind})]),
                                                     ddk.Block(width=30,
                                                               children=[ddk.Block(BTC_fil['rates_x'][ind],
                                                                                   style={'text-align': 'center'},
                                                                                   id={'type':"urate1", 'index':ind}),
                                                                         ddk.Block("-->>",style={'text-align': 'center'})]),
                                                     ddk.Block(width=30,
                                                               children=[ddk.Block(step, style={"text-align":"right"},
                                                                                   id={'type':"uval2_vol", 'index':ind}),
                                                                         ddk.Block(BTC_fil['valin_y'][ind],
                                                                                   style={"text-align":"right"},
                                                                                   id={'type':"uval2", 'index':ind})]),
                                                     ]))),

                    html.Tr(html.Td(style={'padding': '0'},
                                    children=
                                    ddk.Block(width=100,
                                              style={'width': '600px'},
                                              children=[
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(step,
                                                                                id={'type':"uval3_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil['valin_y'][ind],
                                                                                id={'type':"uval3", 'index':ind})]),
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(BTC_fil['rates_y'][ind],
                                                                                style={'text-align': 'center'},
                                                                                id={'type':"urate2", 'index':ind}),
                                                                      ddk.Block("-->>", style={'text-align': 'center'})]),
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(step2,style={"font-weight": "700",
                                                                                             "text-align":"right"},
                                                                                id={'type':"uval4_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil['valout_y'][ind],
                                                                                style={"text-align":"right"},
                                                                                id={'type':"uval4", 'index':ind})]),
                                              ])
                                    ))]),  # Direction
                html.Td([
                    html.Tr(BTC_fil['perc'][ind], style={"font-weight": "700"},)
                ]),  # Profit
                html.Td([
                    html.Tr(
                            style={'text-align': 'center'},
                            children=[html.Button("Go !",
                                              style={'text-align': 'center', 'max-width': '100px',
                                                         "background-color": "palegreen",
                                                         "border-radius": "20px",
                                                         'font-size': '15px'},
                                              n_clicks=0,
                                              id={'type':"uorder_btn", 'index':ind})])
                ]),  # Button
                html.Td([
                    html.Tr([], id={'type':"uorder_result", 'index':ind})
                ])  # Result
            ]))
    else:
        pass

    if BTC_fil_main.shape[0]>0:
        for ind in BTC_fil_main.index:
            rate1 = (BTC_fil_main['start'][ind] / BTC_fil_main['step'][ind])
            rate2 = (BTC_fil_main['back'][ind] / BTC_fil_main['step'][ind])
            step = (BTC_fil_main['volume'][ind] * rate1)
            step2 = (rate2 * BTC_fil_main['volume'][ind])
            rows.append(html.Tr([
                html.Td(style={'text-align': 'center'},
                        children=[ddk.Block(BTC_fil_main['TIME'][ind]),ddk.Block(BTC_fil_main['timer'][ind]),
                                  ddk.Block(id={'type': "uregim",'index': ind},
                                            children=BTC_fil_main['regim'][ind])]),

                html.Td([
                    html.Tr(BTC_fil_main['birga_x'][ind],
                            id={'type': "ubirga_1", 'index': ind}),
                    html.Tr(BTC_fil_main['birga_y'][ind],
                            id={'type': "ubirga_2", 'index': ind})

                ]),

                html.Td(style={'padding': '0'},
                        children=[
                            html.Tr(html.Td(style={'padding': '0'},
                                            children=
                                            ddk.Block(width=100,
                                                      style={'width': '600px'},
                                                      children=[
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(step, style={"font-weight": "700"},
                                                                                        id={'type': "uval1_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(BTC_fil_main['valin_x'][ind],
                                                                                        id={'type': "uval1",
                                                                                            'index': ind})]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(BTC_fil_main['rates_x'][ind],
                                                                                        style={'text-align': 'center'},
                                                                                        id={'type':"urate1", 'index':ind}),
                                                                              ddk.Block("-->>")]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(BTC_fil_main['volume'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval2_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(BTC_fil_main['valin_y'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval2",
                                                                                            'index': ind})]),
                                                      ]))),

                            html.Tr(html.Td(style={'padding': '0'},
                                            children=
                                            ddk.Block(width=100,
                                                      style={'width': '600px'},
                                                      children=[
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(BTC_fil_main['volume'][ind],
                                                                                        id={'type': "uval3_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(BTC_fil_main['valin_y'][ind],
                                                                                        id={'type': "uval3",
                                                                                            'index': ind})]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(BTC_fil_main['rates_y'][ind],
                                                                                        style={'text-align': 'center'},
                                                                                        id={'type':"urate2", 'index':ind} ),
                                                                              ddk.Block("-->>")]),
                                                          ddk.Block(width=30,
                                                                    children=[ddk.Block(step2, style={"font-weight": "700",
                                                                                                      "text-align": "right"},
                                                                                        id={'type': "uval4_vol",
                                                                                            'index': ind}),
                                                                              ddk.Block(BTC_fil_main['valout_y'][ind],
                                                                                        style={"text-align": "right"},
                                                                                        id={'type': "uval4",
                                                                                            'index': ind})]),
                                                      ])
                                            ))]),

                html.Td([
                    html.Tr(BTC_fil_main['perc'][ind], style={"font-weight": "700"})
                ]),

                html.Td([
                    html.Tr(
                        style={'text-align': 'center'},
                        children=[html.Button("Go !",
                                              style={'text-align': 'center', 'max-width': '100px',
                                                     "background-color": "palegreen",
                                                     "border-radius": "20px",
                                                     'font-size': '15px'},
                                              n_clicks=0,
                                              id={'type': "uorder_btn", 'index': ind})])
                ]),

                html.Td([html.Tr([], id={'type': "uorder_result", 'index': ind})])

            ]))
    else:
        pass

    if BTC_fil_main2.shape[0] > 0:
        for ind in BTC_fil_main2.index:
            rate1 = (BTC_fil_main2['step'][ind] / BTC_fil_main2['start'][ind])
            rate2 = (BTC_fil_main2['step'][ind] / BTC_fil_main2['back'][ind])
            step = (BTC_fil_main2['volume'][ind] * rate1)
            step2 =(step / rate2)
            rows.append(html.Tr([
                html.Td(style={'text-align': 'center'}, children=[ddk.Block(BTC_fil_main2['TIME'][ind]),ddk.Block(BTC_fil_main2['timer'][ind]),
                                  ddk.Block(id={'type': "uregim",'index': ind},
                                            children=BTC_fil_main2['regim'][ind])]),
                html.Td([
                    html.Tr(BTC_fil_main2['birga_x'][ind],
                                    id={'type':"ubirga_1", 'index':ind}),
                    html.Tr(BTC_fil_main2['birga_y'][ind],
                                    id={'type':"ubirga_2", 'index':ind})

                ]),   # Birga
                html.Td(style={'padding': '0'}, children=[
                    html.Tr(html.Td(style={'padding': '0'},
                                    children=
                                    ddk.Block(width=100,
                                              style={'width': '600px'},
                                              children=[
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(BTC_fil_main2['volume'][ind],
                                                                                style={"font-weight": "700"},
                                                                                id={'type':"uval1_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil_main2['valin_x'][ind],
                                                                                id={'type':"uval1", 'index':ind})]),
                                                     ddk.Block(width=30,
                                                               children=[ddk.Block(BTC_fil_main2['rates_x'][ind],
                                                                                   style={'text-align': 'center'},
                                                                                   id={'type':"urate1", 'index':ind}),
                                                                         ddk.Block("-->>",style={'text-align': 'center'})]),
                                                     ddk.Block(width=30,
                                                               children=[ddk.Block(step, style={"text-align":"right"},
                                                                                   id={'type':"uval2_vol", 'index':ind}),
                                                                         ddk.Block(BTC_fil_main2['valin_y'][ind],
                                                                                   style={"text-align":"right"},
                                                                                   id={'type':"uval2", 'index':ind})]),
                                                     ]))),

                    html.Tr(html.Td(style={'padding': '0'},
                                    children=
                                    ddk.Block(width=100,
                                              style={'width': '600px'},
                                              children=[
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(step,
                                                                                id={'type':"uval3_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil_main2['valin_y'][ind],
                                                                                id={'type':"uval3", 'index':ind})]),
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(BTC_fil_main2['rates_y'][ind],
                                                                                style={'text-align': 'center'},
                                                                                id={'type':"urate2", 'index':ind}),
                                                                      ddk.Block("-->>", style={'text-align': 'center'})]),
                                                  ddk.Block(width=30,
                                                            children=[ddk.Block(step2,style={"font-weight": "700",
                                                                                             "text-align":"right"},
                                                                                id={'type':"uval4_vol", 'index':ind}),
                                                                      ddk.Block(BTC_fil_main2['valout_y'][ind],
                                                                                style={"text-align":"right"},
                                                                                id={'type':"uval4", 'index':ind})]),
                                              ])
                                    ))]),  # Direction
                html.Td([
                    html.Tr(BTC_fil_main2['perc'][ind], style={"font-weight": "700"},)
                ]),  # Profit
                html.Td([
                    html.Tr(
                            style={'text-align': 'center'},
                            children=[html.Button("Go !",
                                              style={'text-align': 'center', 'max-width': '100px',
                                                         "background-color": "palegreen",
                                                         "border-radius": "20px",
                                                         'font-size': '15px'},
                                              n_clicks=0,
                                              id={'type':"uorder_btn", 'index':ind})])
                ]),  # Button
                html.Td([
                    html.Tr([], id={'type':"uorder_result", 'index':ind})
                ])  # Result
            ]))
    else:
        pass


    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_body,
                      bordered=True,
                      dark=True,
                      hover=True,
                      responsive=True,
                      striped=True,
                      style={'width':"100%"})

    return table

