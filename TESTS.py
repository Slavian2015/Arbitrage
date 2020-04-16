import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import json



#####################    ADD NEW EMPTY REGIM    #######################

# main_path_data = os.path.abspath("./data")
# f = open(main_path_data + "\\regim.json")
# com = json.load(f)
# print("AFTER :", com)



def create():
    with open(main_path_data + "\\regim.json", "r") as file:
        param = []
        data = json.load(file)
        file.close()
        for k, v in data.items():
            param.append(k)
        next_id = str(int(param[-1]) +1)
        data[next_id] = {"option": "off", "val1": "", "val2": "", "val3": "", "birga1": "", "birga2": "", "profit": "",
                        "order": "", "per": ""}
        f = open(main_path_data + "\\regim.json", "w")
        json.dump(data, f)
        # print("BEFORE2 :", data)
        f.close()
create()


def group_of_regims():
    main_path_data = os.path.abspath("./data")
    f = open(main_path_data + "\\regim.json")
    com = json.load(f)

    group_of_regims = []


    for k,v in com.items():
        list_item = dbc.ListGroupItem(style={
        'line-height': '1', 'margin': '0', 'margin-right': '0',
        'height': 'fit-content', 'justify-content': 'center',
        'vertical-align': '-webkit-baseline-middle',
        'max-height': 'fit-content', 'padding': '0px',
        'list-style': 'none',
        'align-items': 'center'},
        children=ddk.Card(
            style={'width': '100%',
                 'margin': '0',
                 'margin-top': '10px',
                 'background-color': '#e4e7e7a6'},
            card_hover=True,
            children=ddk.Block(
                  width=100,
                  style={'justify-content': 'center',
                         'vertical-align': '-webkit-baseline-middle'},
                  children=[ddk.Block(width=5,
                                      style={'vertical-align': '-webkit-baseline-middle'},
                                      children=html.H2("{}".format(v['option']),
                                                       id="option_{}".format(k),
                                                       style={'margin': '0',
                                                              'text-align': 'center',
                                                              'vertical-align': '-webkit-baseline-middle',
                                                              'justify-content': 'center'})),
                              ddk.Block(width=45,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id="val1_{}".format(k),
                                                                                    style={'background-color': '#fff'},
                                                                                    options=[
                                                                                  {'label': 'BTC', 'value': 'BTC'},
                                                                                  {'label': 'USD', 'value': 'USD'},
                                                                                  {'label': 'USDt', 'value': 'USDt'},
                                                                                  {'label': 'ETH', 'value': 'ETH'}
                                                                                                      ],
                                                                                    value='')),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id="val2_{}".format(k),
                                                                                    style={'background-color': '#fff'},
                                                                                    options=[
                                                                                  {'label': 'BTC', 'value': 'BTC'},
                                                                                  {'label': 'USD', 'value': 'USD'},
                                                                                  {'label': 'USDt', 'value': 'USDt'},
                                                                                  {'label': 'ETH', 'value': 'ETH'}
                                                                                                      ],
                                                                                    value='')),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=dcc.Dropdown(
                                                                                    id="val3_{}".format(k),
                                                                                    style={'background-color': '#fff'},
                                                                                    options=[
                                                                                  {'label': 'BTC', 'value': 'BTC'},
                                                                                  {'label': 'USD', 'value': 'USD'},
                                                                                  {'label': 'USDt', 'value': 'USDt'},
                                                                                  {'label': 'ETH', 'value': 'ETH'}
                                                                                                      ],
                                                                                    value=''))

                                                                      ]),
                                                  ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                                children=[
                                                                ddk.Block(width=40,
                                                                          style={'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id="b1_{}".format(k),
                                                                              style={'background-color': '#fff'},
                                                                              placeholder="БИРЖА 1",
                                                                              options=[
                                                                                    {
                                                                                        'label': 'alfa',
                                                                                        'value': 'alfa'},
                                                                                    {
                                                                                        'label': 'hot',
                                                                                        'value': 'hot'},
                                                                                    {
                                                                                        'label': 'live',
                                                                                        'value': 'live'},

                                                                                                ],
                                                                                                value='')),
                                                                ddk.Block(width=40,
                                                                          style={
                                                                              'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id="b2_{}".format(k),
                                                                              placeholder="БИРЖА 2",
                                                                              style={'background-color': '#fff'},
                                                                              options=[
                                                                                  {
                                                                                      'label': 'alfa',
                                                                                      'value': 'alfa'},
                                                                                  {
                                                                                      'label': 'hot',
                                                                                      'value': 'hot'},
                                                                                  {
                                                                                      'label': 'live',
                                                                                      'value': 'live'},
                                                                              ],
                                                                              value=''))
                                                                ]),
                                                  ]),

                              ddk.Block(width=50,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5('% profit',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                id="profit_r1_{}".format(k),
                                                                                                placeholder=v['profit'],
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0','text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                placeholder=v['order'],
                                                                                                id="order_r1_{}".format(
                                                                                                    k),
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0','text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                placeholder=v['per'],
                                                                                                id="perc_r1_{}".format(
                                                                                                    k),
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'text-align': 'left',
                                                                                                    'margin': '0',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=10,
                                                                                children=[dbc.Checklist(
                                                                                    style={'text-align': 'center',
                                                                                           'border': '#333',
                                                                                           'vertical-align': '-webkit-baseline-middle',
                                                                                           'justify-content': 'center'},
                                                                                    options=[
                                                                                            {"label": "Off",
                                                                                             "value": 1}
                                                                                                        ],
                                                                                    value=[],
                                                                                    id="checklist_r1_{}".format(
                                                                                                    k),
                                                                                    inline=True)

                                                                                          ])]),
                                                  ddk.Block(width=100,
                                                            style={'margin-top': '5px',
                                                                 'margin-bottom': '5px',
                                                                 'vertical-align': '-webkit-baseline-middle',
                                                                 'border-top-style': 'groove',
                                                                 'border-bottom-style': 'groove'},
                                                            children=[
                                                                ddk.Block(width=100,
                                                                          style={
                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                          children=[ddk.Block(
                                                                              width=30,
                                                                              children=[
                                                                                  ddk.Block(
                                                                                      width=50,
                                                                                      style={
                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                      children=[
                                                                                          html.H5(
                                                                                              '% profit',
                                                                                              style={
                                                                                                  'text-align': 'right',
                                                                                                  'justify-content': 'center'})]),
                                                                                  ddk.Block(
                                                                                      width=50,
                                                                                      style={
                                                                                          'text-align': 'left',
                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                      children=[
                                                                                          dcc.Input(
                                                                                              style={
                                                                                                  'border': 'double',
                                                                                                  'margin': '0',
                                                                                                  'text-align': 'left',
                                                                                                  'background-color': 'ivory',
                                                                                                  'width': '-webkit-fill-available',
                                                                                                  'max-width': '60px'})])]),
                                                                              ddk.Block(
                                                                                  width=30,
                                                                                  children=[
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              html.H5(
                                                                                                  'V ордера',
                                                                                                  style={
                                                                                                      'text-align': 'right',
                                                                                                      'justify-content': 'center'})]),
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'text-align': 'left',
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              dcc.Input(
                                                                                                  style={
                                                                                                      'border': 'double',
                                                                                                      'margin': '0',
                                                                                                      'text-align': 'left',
                                                                                                      'background-color': 'ivory',
                                                                                                      'width': '-webkit-fill-available',
                                                                                                      'max-width': '60px'})])]),
                                                                              ddk.Block(
                                                                                  width=30,
                                                                                  children=[
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              html.H5(
                                                                                                  '% ордера',
                                                                                                  style={
                                                                                                      'text-align': 'right',
                                                                                                      'justify-content': 'center'})]),
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'text-align': 'left',
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              dcc.Input(
                                                                                                  style={
                                                                                                      'border': 'double',
                                                                                                      'text-align': 'left',
                                                                                                      'margin': '0',
                                                                                                      'background-color': 'ivory',
                                                                                                      'width': '-webkit-fill-available',
                                                                                                      'max-width': '60px'})])]),
                                                                              ddk.Block(
                                                                                  width=10,
                                                                                  children=[])]),
                                                                ddk.Block(width=100,
                                                                          style={
                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                          children=[ddk.Block(width=30,
                                                                                              style={'margin-top': '5px', 'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              'секунд',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'text-align': 'left','vertical-align':
                                                                                                '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'margin': '0','text-align': 'left',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  'max-width': '60px'})])]),
                                                                                    ddk.Block(width=30,
                                                                                              style={'margin-top': '5px', 'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '1я Ставка (%)',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'margin': '0','text-align': 'left',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  'max-width': '60px'})])]),
                                                                                    ddk.Block(width=30,
                                                                                              style={'margin-top': '5px', 'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '2я Ставка (%)',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'text-align': 'left',
                                                                                                                  'margin': '0',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  'max-width': '60px'})])]),
                                                                                    ddk.Block(width=10,
                                                                                              style={'margin-top': '5px', 'margin-bottom': '5px'},
                                                                                              children=[dbc.Checklist(style={'text-align': 'center',
                                                                                                                             'border': '#333',
                                                                                                                             'vertical-align': '-webkit-baseline-middle',
                                                                                                                             'justify-content': 'center'},
                                                                                                                      options=[
                                                                                                                          {"label": "Off",
                                                                                                                           "value": 1}
                                                                                                                      ],
                                                                                                                      value=[],
                                                                                                                      id="checklist-r2-input{}".format(
                                                                                                    k),
                                                                                                                      inline=True)

                                                                                                        ])])
                                                            ]),
                                                  ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% profit',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0','text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0','text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'text-align': 'left',
                                                                                                    'margin': '0',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=10,
                                                                                children=[dbc.Checklist(style={'text-align': 'center',
                                                                                                               'border': '#333',
                                                                                                               'vertical-align': '-webkit-baseline-middle',
                                                                                                               'justify-content': 'center'},
                                                                                                        options=[
                                                                                                            {"label": "Off",
                                                                                                             "value": 1}
                                                                                                        ],
                                                                                                        value=[],
                                                                                                        id="checklist-r3-input{}".format(
                                                                                                            k),
                                                                                                        inline=True)

                                                                                          ])])]
                                        )])))

        group_of_regims.append(list_item)


    return group_of_regims



for i in group_of_regims():
    print(i)
# print(len(group_of_regims()))