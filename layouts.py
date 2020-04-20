import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import pandas as pd
import dash_table
import os
from app import dash_app
import os
from VILKA import valuta
import json
import pandas as pd


main_path_data = os.path.abspath("./data")

my_col=['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y', 'volume_x',
                 'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']
final = pd.DataFrame(columns=my_col)


f = open(main_path_data + "\\commis.json")
com = json.load(f)

###########  Main Page   ################

# def serve_layout():
#     """Creates the layout for each user of the app.
#     This function is executed each time a session is created for the app.
#     It creates a new session id (a uuid.uuid1 as string) each time.
#
#     This session id will be used in combination with a DashDatabase instance to manage user values.
#     It will be fetched via the property data of a dcc.Store component.
#     """
#
#     # create a session id
#     session_id = str(uuid.uuid1())
#     # store the session id in a dcc.Store component (invisible component for storing data)
#     store_session_id_div = dcc.Store(id='session_id_div_id',
#                                      storage_type='session',  # IMPORTANT! see docstring of dcc.Store
#                                      data=session_id)
#
#     # create tab to enter a value
#     first_tab = dcc.Tab(label="Enter a value",
#                         children=[dcc.Input(placeholder="Enter value here", id="input_div"),
#                                   html.Button(children="OK", id="ok_button"),
#                                   dcc.Markdown(id="success_value_saved")])
#
#     # create tab to retrieve the value entered in the other tab
#     second_tab = dcc.Tab(label="Retrieve the value",
#                          children=[html.Button(children="Show me the value", id="show_value_button"),
#                                    dcc.Markdown(id="show_value_div")])
#
#     # assemble tabs in dcc.Tabs object
#     tabs = dcc.Tabs(children=[first_tab, second_tab])
#
#     # create layout
#     layout = html.Div(children=[tabs, store_session_id_div])
#
#     return layout
# layout_main = serve_layout()



########  MAIN PAGE MY  ##############

def group_of_regims():
    # main_path_data = os.path.abspath("./data")
    d = open(main_path_data + "\\regim.json")
    com2 = json.load(d)

    group_of_regims = []
    html.Div(id='hidden-div')

    param_head = ddk.Card(style={'width': '100%', 'line-height': '1',
                                 'height': '70px', 'margin': '0', 'max-height': 'fit-content',
                                 'background-color': '#fff'},
                          shadow_weight='heavy',
                          children=ddk.Block(width=100,
                                             style={'justify-content': 'center'},
                                             children=[ddk.Block(width=5,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('Active',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                       ddk.Block(width=45,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=[
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'})),
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'})),
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'}))]),
                                                       ddk.Block(width=45,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('PARAMETERS',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                       ddk.Block(width=5,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('Signal (on/off)',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'}))]))

    group_of_regims.append(param_head)

    for k, v in com2.items():
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
                                        children=[html.H2(
                                            id={
                                                 'type': 'option',
                                                 'index': k
                                             },
                                            style={'margin': '0',
                                                'text-align': 'center',
                                                'vertical-align': '-webkit-baseline-middle',
                                                'justify-content': 'center'},
                                            children=[v['option']]),


                                                  ]),
                              ddk.Block(width=45,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val1',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDt',
                                                                                         'value': 'USDt'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'}
                                                                                    ],
                                                                                    value='{}'.format(v["val1"]))),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val2',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDt',
                                                                                         'value': 'USDt'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'}
                                                                                    ],
                                                                                    value='{}'.format(v["val2"]))),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val3',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDt',
                                                                                         'value': 'USDt'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'}
                                                                                    ],
                                                                                    value='{}'.format(v["val3"])))

                                                                      ]),
                                                  ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[
                                                                ddk.Block(width=40,
                                                                          style={'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'birga1',
                                                                                  'index': k
                                                                              },
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
                                                                              value='{}'.format(v["birga1"]))),
                                                                ddk.Block(width=40,
                                                                          style={
                                                                              'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'birga2',
                                                                                  'index': k
                                                                              },
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
                                                                              value='{}'.format(v["birga2"])))
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
                                                                                        style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5('% profit',
                                                                                                    style={
                                                                                                        'text-align': 'right',
                                                                                                        'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(v["profit"]),
                                                                                                id={
                                                                                                    'type': 'profit',
                                                                                                    'index': k
                                                                                                },
                                                                                                placeholder=v[
                                                                                                    'profit'],
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(
                                                                                                    v["order"]),
                                                                                                placeholder=v[
                                                                                                    'order'],
                                                                                                id={
                                                                                                    'type': 'order',
                                                                                                    'index': k
                                                                                                },
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    'max-width': '60px'})])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(
                                                                                                    v["per"]),
                                                                                                placeholder=v['per'],
                                                                                                id={
                                                                                                    'type': 'percent',
                                                                                                    'index': k
                                                                                                },
                                                                                                style={
                                                                'border': 'double',
                                                                'text-align': 'left',
                                                                'margin': '0',
                                                                'background-color': 'ivory',
                                                                'width': '-webkit-fill-available',
                                                                'max-width': '60px'})])]),
                                                                      ddk.Block(width=10,
                                                                                children=[

                                                                dcc.Checklist(
                                                                    id={
                                                                    'type': 'checklist',
                                                                    'index': k
                                                                },
                                                                # style={'text-align': 'center',
                                                                #        'border': '#333',
                                                                #        'vertical-align': '-webkit-baseline-middle',
                                                                #        'justify-content': 'center'},
                                                                options=[
                                                                    {"label": "on/off",
                                                                     "value": "active"},
                                                                ],
                                                                value=[],
                                                                style={"display": "inline"},
                                                                labelStyle={"display": "inline"}

                                                                )

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
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              'секунд',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'text-align': 'left',
                                                                                                          'vertical-align':
                                                                                                              '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'margin': '0',
                                                                                                                  'text-align': 'left',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  'max-width': '60px'})])]),
                                                                                    ddk.Block(width=30,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '1я Ставка (%)',
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
                                                                                    ddk.Block(width=30,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '2я Ставка (%)',
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
                                                                                    ddk.Block(width=10,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  dbc.Checklist(
                                                                                                      style={
                                                                                                          'text-align': 'center',
                                                                                                          'border': '#333',
                                                                                                          'vertical-align': '-webkit-baseline-middle',
                                                                                                          'justify-content': 'center'},
                                                                                                      options=[
                                                                                                          {
                                                                                                              "label": "Off",
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
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% profit',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
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
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
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
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
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
                                                                                    id="checklist-r3-input{}".format(
                                                                                        k),
                                                                                    inline=True)

                                                                                ])])]
                                        )])))

        group_of_regims.append(list_item)
    return group_of_regims






# print(len(group_of_regims()))

def serve_layout():


    # list_group = [i for i in group_of_regims()]




    # param_val = ddk.Card(style={'width': '100%', 'margin': '0', 'margin-top': '10px',
    #                             'background-color': '#e4e7e7a6'},
    #                      card_hover=True,
    #                      children=ddk.Block(width=100,
    #                                         style={'justify-content': 'center',
    #                                                'vertical-align': '-webkit-baseline-middle',},
    #                                         children=[ddk.Block(width=5,
    #                                                             style={'vertical-align': '-webkit-baseline-middle'},
    #                                                             children=html.H2('Active', style={'margin': '0',
    #                                                                                              'text-align': 'center',
    #                                                                                              'vertical-align': '-webkit-baseline-middle',
    #                                                                                              'justify-content': 'center'})),
    #                                                   ddk.Block(width=45,
    #                                                             style={'vertical-align': '-webkit-baseline-middle'},
    #                                                             children=[ddk.Block(width=100,
    #                                                                                 style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                 children=[ddk.Block(width=30,
    #                                                                                                     style={'margin': '5px',},
    #                                                                                                     children=dcc.Dropdown(style={'background-color': '#fff'},
    #                                                                                         options=[
    #                                                                                             {'label': 'BTC', 'value': 'BTC'},
    #                                                                                             {'label': 'USD', 'value': 'USD'},
    #                                                                                             {'label': 'USDt', 'value': 'USDt'},
    #                                                                                             {'label': 'ETH', 'value': 'ETH'}
    #                                                                                         ],
    #                                                                                         value='')),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     style={'margin': '5px'},
    #                                                                                                     children=dcc.Dropdown(style={'background-color': '#fff'},
    #                                                                                         options=[
    #                                                                                             {'label': 'BTC', 'value': 'BTC'},
    #                                                                                             {'label': 'USD', 'value': 'USD'},
    #                                                                                             {'label': 'USDt', 'value': 'USDt'},
    #                                                                                             {'label': 'ETH', 'value': 'ETH'}
    #                                                                                         ],
    #                                                                                         value='')),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     style={'margin': '5px'},
    #                                                                                                     children=dcc.Dropdown(style={'background-color': '#fff'},
    #                                                                                         options=[
    #                                                                                             {'label': 'BTC', 'value': 'BTC'},
    #                                                                                             {'label': 'USD', 'value': 'USD'},
    #                                                                                             {'label': 'USDt', 'value': 'USDt'},
    #                                                                                             {'label': 'ETH', 'value': 'ETH'}
    #                                                                                         ],
    #                                                                                         value=''))
    #
    #                                                                                           ]),
    #                                                                       ddk.Block(width=100,
    #                                                                                 style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                 children=[
    #                                                                                     ddk.Block(width=40,
    #                                                                                               style={'margin': '5px'},
    #                                                                                               children=dcc.Dropdown(style={'background-color': '#fff'},
    #                                                                                                                     placeholder="БИРЖА 1",
    #                                                                                                       options=[
    #                                                                                                           {
    #                                                                                                               'label': 'alfa',
    #                                                                                                               'value': 'alfa'},
    #                                                                                                           {
    #                                                                                                               'label': 'hot',
    #                                                                                                               'value': 'hot'},
    #                                                                                                           {
    #                                                                                                               'label': 'live',
    #                                                                                                               'value': 'live'},
    #
    #                                                                                                         ],
    #                                                                                                       value='')),
    #                                                                                           ddk.Block(width=40,
    #                                                                                                     style={
    #                                                                                                         'margin': '5px'},
    #                                                                                                     children=dcc.Dropdown(
    #                                                                                                         placeholder="БИРЖА 2",
    #                                                                                                         style={
    #                                                                                                             'background-color': '#fff'},
    #                                                                                                         options=[
    #                                                                                                             {
    #                                                                                                                 'label': 'alfa',
    #                                                                                                                 'value': 'alfa'},
    #                                                                                                             {
    #                                                                                                                 'label': 'hot',
    #                                                                                                                 'value': 'hot'},
    #                                                                                                             {
    #                                                                                                                 'label': 'live',
    #                                                                                                                 'value': 'live'},
    #                                                                                                         ],
    #                                                                                                         value=''))
    #
    #
    #
    #
    #
    #
    #
    #                                                                                           ]),
    #                                                                         ]),
    #
    #                                                   ddk.Block(width=50,
    #                                                             style={'vertical-align': '-webkit-baseline-middle'},
    #                                                             children=[ddk.Block(width=100,
    #                                                                                 style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                 children=[ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     html.H5(
    #                                                                                                                         '% profit',
    #                                                                                                                         style={
    #                                                                                                                             'text-align': 'right',
    #                                                                                                                             'justify-content': 'center'})]),
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     dcc.Input(
    #                                                                                                                         style={
    #                                                                                                                             'border': 'double',
    #                                                                                                                             'margin': '0','text-align': 'left',
    #                                                                                                                             'background-color': 'ivory',
    #                                                                                                                             'width': '-webkit-fill-available',
    #                                                                                                                             'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         html.H5(
    #                                                                                                                                             'V ордера',
    #                                                                                                                                             style={
    #                                                                                                                                                 'text-align': 'right',
    #                                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         dcc.Input(
    #                                                                                                                                             style={
    #                                                                                                                                                 'border': 'double',
    #                                                                                                                                                 'margin': '0','text-align': 'left',
    #                                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         html.H5(
    #                                                                                                                                             '% ордера',
    #                                                                                                                                             style={
    #                                                                                                                                                 'text-align': 'right',
    #                                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         dcc.Input(
    #                                                                                                                                             style={
    #                                                                                                                                                 'border': 'double',
    #                                                                                                                                                 'text-align': 'left',
    #                                                                                                                                                 'margin': '0',
    #                                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=10,
    #                                                                                                     children=[dbc.Checklist(style={'text-align': 'center',
    #                                                                                                               'border': '#333',
    #                                                                                                               'vertical-align': '-webkit-baseline-middle',
    #                                                                                                               'justify-content': 'center'},
    #                                                                                                        options=[
    #                                                                                                            {"label": "Off",
    #                                                                                                             "value": 1}
    #                                                                                                        ],
    #                                                                                                        value=[],
    #                                                                                                        id="checklist-inline-input",
    #                                                                                                        inline=True)
    #
    #                                                                                                     ])]),
    #                                                                       ddk.Block(width=100,
    #                                                                                 style={'margin-top': '5px',
    #                                                                                        'margin-bottom': '5px',
    #                                                                                        'vertical-align': '-webkit-baseline-middle',
    #                                                                                        'border-top-style': 'groove',
    #                                                                                        'border-bottom-style': 'groove'},
    #                                                                                 children=[
    #                                                                                     ddk.Block(width=100,
    #                                                                                               style={
    #                                                                                                   'vertical-align': '-webkit-baseline-middle'},
    #                                                                                               children=[ddk.Block(
    #                                                                                                   width=30,
    #                                                                                                   children=[
    #                                                                                                       ddk.Block(
    #                                                                                                           width=50,
    #                                                                                                           style={
    #                                                                                                               'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                           children=[
    #                                                                                                               html.H5(
    #                                                                                                                   '% profit',
    #                                                                                                                   style={
    #                                                                                                                       'text-align': 'right',
    #                                                                                                                       'justify-content': 'center'})]),
    #                                                                                                       ddk.Block(
    #                                                                                                           width=50,
    #                                                                                                           style={
    #                                                                                                               'text-align': 'left',
    #                                                                                                               'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                           children=[
    #                                                                                                               dcc.Input(
    #                                                                                                                   style={
    #                                                                                                                       'border': 'double',
    #                                                                                                                       'margin': '0',
    #                                                                                                                       'text-align': 'left',
    #                                                                                                                       'background-color': 'ivory',
    #                                                                                                                       'width': '-webkit-fill-available',
    #                                                                                                                       'max-width': '60px'})])]),
    #                                                                                                         ddk.Block(
    #                                                                                                             width=30,
    #                                                                                                             children=[
    #                                                                                                                 ddk.Block(
    #                                                                                                                     width=50,
    #                                                                                                                     style={
    #                                                                                                                         'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                     children=[
    #                                                                                                                         html.H5(
    #                                                                                                                             'V ордера',
    #                                                                                                                             style={
    #                                                                                                                                 'text-align': 'right',
    #                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                 ddk.Block(
    #                                                                                                                     width=50,
    #                                                                                                                     style={
    #                                                                                                                         'text-align': 'left',
    #                                                                                                                         'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                     children=[
    #                                                                                                                         dcc.Input(
    #                                                                                                                             style={
    #                                                                                                                                 'border': 'double',
    #                                                                                                                                 'margin': '0',
    #                                                                                                                                 'text-align': 'left',
    #                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                                         ddk.Block(
    #                                                                                                             width=30,
    #                                                                                                             children=[
    #                                                                                                                 ddk.Block(
    #                                                                                                                     width=50,
    #                                                                                                                     style={
    #                                                                                                                         'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                     children=[
    #                                                                                                                         html.H5(
    #                                                                                                                             '% ордера',
    #                                                                                                                             style={
    #                                                                                                                                 'text-align': 'right',
    #                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                 ddk.Block(
    #                                                                                                                     width=50,
    #                                                                                                                     style={
    #                                                                                                                         'text-align': 'left',
    #                                                                                                                         'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                     children=[
    #                                                                                                                         dcc.Input(
    #                                                                                                                             style={
    #                                                                                                                                 'border': 'double',
    #                                                                                                                                 'text-align': 'left',
    #                                                                                                                                 'margin': '0',
    #                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                                         ddk.Block(
    #                                                                                                             width=10,
    #                                                                                                             children=[])]),
    #                                                                                     ddk.Block(width=100,
    #                                                                                               style={
    #                                                                                                   'vertical-align': '-webkit-baseline-middle'},
    #                                                                                               children=[ddk.Block(width=30,
    #                                                                                                     style={'margin-top': '5px', 'margin-bottom': '5px'},
    #                                                                                                     children=[
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     html.H5(
    #                                                                                                                         'секунд',
    #                                                                                                                         style={
    #                                                                                                                             'text-align': 'right',
    #                                                                                                                             'justify-content': 'center'})]),
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     dcc.Input(
    #                                                                                                                         style={
    #                                                                                                                             'border': 'double',
    #                                                                                                                             'margin': '0','text-align': 'left',
    #                                                                                                                             'background-color': 'ivory',
    #                                                                                                                             'width': '-webkit-fill-available',
    #                                                                                                                             'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     style={'margin-top': '5px', 'margin-bottom': '5px'},
    #                                                                                                     children=[
    #                                                                                                     ddk.Block(
    #                                                                                                         width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                         children=[
    #                                                                                                             html.H5(
    #                                                                                                                 '1я Ставка (%)',
    #                                                                                                                 style={
    #                                                                                                                     'text-align': 'right',
    #                                                                                                                     'justify-content': 'center'})]),
    #                                                                                                     ddk.Block(
    #                                                                                                         width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                         children=[
    #                                                                                                             dcc.Input(
    #                                                                                                                 style={
    #                                                                                                                     'border': 'double',
    #                                                                                                                     'margin': '0','text-align': 'left',
    #                                                                                                                     'background-color': 'ivory',
    #                                                                                                                     'width': '-webkit-fill-available',
    #                                                                                                                     'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     style={'margin-top': '5px', 'margin-bottom': '5px'},
    #                                                                                                     children=[
    #                                                                                                     ddk.Block(
    #                                                                                                         width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                         children=[
    #                                                                                                             html.H5(
    #                                                                                                                 '2я Ставка (%)',
    #                                                                                                                 style={
    #                                                                                                                     'text-align': 'right',
    #                                                                                                                     'justify-content': 'center'})]),
    #                                                                                                     ddk.Block(
    #                                                                                                         width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                         children=[
    #                                                                                                             dcc.Input(
    #                                                                                                                 style={
    #                                                                                                                     'border': 'double',
    #                                                                                                                     'text-align': 'left',
    #                                                                                                                     'margin': '0',
    #                                                                                                                     'background-color': 'ivory',
    #                                                                                                                     'width': '-webkit-fill-available',
    #                                                                                                                     'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=10,
    #                                                                                                     style={'margin-top': '5px', 'margin-bottom': '5px'},
    #                                                                                                     children=[dbc.Checklist(style={'text-align': 'center',
    #                                                                                                               'border': '#333',
    #                                                                                                               'vertical-align': '-webkit-baseline-middle',
    #                                                                                                               'justify-content': 'center'},
    #                                                                                                        options=[
    #                                                                                                            {"label": "Off",
    #                                                                                                             "value": 1}
    #                                                                                                        ],
    #                                                                                                        value=[],
    #                                                                                                        id="checklist-inline-input",
    #                                                                                                        inline=True)
    #
    #                                                                                                     ])])
    #                                                                                 ]),
    #                                                                       ddk.Block(width=100,
    #                                                                                 style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                 children=[ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     html.H5(
    #                                                                                                                         '% profit',
    #                                                                                                                         style={
    #                                                                                                                             'text-align': 'right',
    #                                                                                                                             'justify-content': 'center'})]),
    #                                                                                                             ddk.Block(
    #                                                                                                                 width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                 children=[
    #                                                                                                                     dcc.Input(
    #                                                                                                                         style={
    #                                                                                                                             'border': 'double',
    #                                                                                                                             'margin': '0','text-align': 'left',
    #                                                                                                                             'background-color': 'ivory',
    #                                                                                                                             'width': '-webkit-fill-available',
    #                                                                                                                             'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         html.H5(
    #                                                                                                                                             'V ордера',
    #                                                                                                                                             style={
    #                                                                                                                                                 'text-align': 'right',
    #                                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'text-align': 'left','vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         dcc.Input(
    #                                                                                                                                             style={
    #                                                                                                                                                 'border': 'double',
    #                                                                                                                                                 'margin': '0','text-align': 'left',
    #                                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=30,
    #                                                                                                     children=[
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         html.H5(
    #                                                                                                                                             '% ордера',
    #                                                                                                                                             style={
    #                                                                                                                                                 'text-align': 'right',
    #                                                                                                                                                 'justify-content': 'center'})]),
    #                                                                                                                                 ddk.Block(
    #                                                                                                                                     width=50,style={'text-align': 'left', 'vertical-align': '-webkit-baseline-middle'},
    #                                                                                                                                     children=[
    #                                                                                                                                         dcc.Input(
    #                                                                                                                                             style={
    #                                                                                                                                                 'border': 'double',
    #                                                                                                                                                 'text-align': 'left',
    #                                                                                                                                                 'margin': '0',
    #                                                                                                                                                 'background-color': 'ivory',
    #                                                                                                                                                 'width': '-webkit-fill-available',
    #                                                                                                                                                 'max-width': '60px'})])]),
    #                                                                                           ddk.Block(width=10,
    #                                                                                                     children=[dbc.Checklist(style={'text-align': 'center',
    #                                                                                                               'border': '#333',
    #                                                                                                               'vertical-align': '-webkit-baseline-middle',
    #                                                                                                               'justify-content': 'center'},
    #                                                                                                        options=[
    #                                                                                                            {"label": "Off",
    #                                                                                                             "value": 1}
    #                                                                                                        ],
    #                                                                                                        value=[],
    #                                                                                                        id="checklist-inline-input",
    #                                                                                                        inline=True)
    #
    #                                                                                                     ])])
    #
    #
    #
    #                                                                       ]
    #
    #
    #                                                             )]))

    # create a session id
    session_id = str(uuid.uuid1())
    # store the session id in a dcc.Store component (invisible component for storing data)
    store_session_id_div = dcc.Store(id='session_id_div_id',
                                     storage_type='session',  # IMPORTANT! see docstring of dcc.Store
                                     data=session_id)

    interval = dcc.Interval(id='interval', interval=10000, n_intervals=0)





    alfa_card = ddk.Card(width=30,
                         style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
                         shadow_weight='heavy',
                         children=[ddk.Block(width=100,
                                             style={'margin':'0'},
                                             children=dbc.ListGroup([
                                                 dbc.ListGroupItem(style={'line-height': '1',
                                                                  'margin': '0', 'margin-right': '0',
                                                                   'justify-content': 'center',
                                                                   'vertical-align': '-webkit-baseline-middle',
                                                                   'max-height': 'fit-content', 'padding': '0px',
                                                                   'list-style': 'none',
                                                                   'align-items': 'center'},
                                                                   active=True,
                                                                   action=True,
                                                                   children= ddk.Block(width=100,
                                                                   children=[ddk.Block(width=20,
                                                                            children=[html.P('Время')]),
                                                                  ddk.Block(width=20,
                                                                            children=[html.P('ПАРА')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('Направление')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('Цена')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('Количество')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('Стоимость')])])),
                             dbc.ListGroupItem(style={'line-height': '1',
                                                      'margin': '0',
                                                      'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                               action=True,
                                               children=ddk.Block(width=100,
                                                                  children=[ddk.Block(width=20,
                                                                children=[html.P('08:54:40')]),
                                                      ddk.Block(width=20,
                                                                children=[html.P('USD/USDT')]),
                                                      ddk.Block(width=15,
                                                                children=[html.P('sell')]),
                                                      ddk.Block(width=15,
                                                                children=[html.P('0,99400000')]),
                                                      ddk.Block(width=15,
                                                                children=[html.P('5,04100000')]),
                                                      ddk.Block(width=15,
                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                        children=[ddk.Block(width=20,
                                                                            children=[html.P('08:54:40')]),
                                                                  ddk.Block(width=20,
                                                                            children=[html.P('USD/USDT')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('sell')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('0,99400000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,04100000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,01075400')])])),
                             dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
'justify-content': 'center',
'vertical-align': '-webkit-baseline-middle',
'max-height': 'fit-content', 'padding': '0px',
'list-style': 'none',
'align-items': 'center'},action=True,
                                               children=ddk.Block(width=100,
                                                        children=[ddk.Block(width=20,
                                                                            children=[html.P('08:54:40')]),
                                                                  ddk.Block(width=20,
                                                                            children=[html.P('USD/USDT')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('sell')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('0,99400000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,04100000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,01075400')])])),
                             dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
'justify-content': 'center',
'vertical-align': '-webkit-baseline-middle',
'max-height': 'fit-content', 'padding': '0px',
'list-style': 'none',
'align-items': 'center'},action=True,
                                               children=ddk.Block(width=100,
                                                        children=[ddk.Block(width=20,
                                                                            children=[html.P('08:54:40')]),
                                                                  ddk.Block(width=20,
                                                                            children=[html.P('USD/USDT')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('sell')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('0,99400000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,04100000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,01075400')])])),
                             dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
'justify-content': 'center',
'vertical-align': '-webkit-baseline-middle',
'max-height': 'fit-content', 'padding': '0px',
'list-style': 'none',
'align-items': 'center'},action=True,
                                               children=ddk.Block(width=100,
                                                        children=[ddk.Block(width=20,
                                                                            children=[html.P('08:54:40')]),
                                                                  ddk.Block(width=20,
                                                                            children=[html.P('USD/USDT')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('sell')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('0,99400000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,04100000')]),
                                                                  ddk.Block(width=15,
                                                                            children=[html.P('5,01075400')])])),

                                                ]))
                                   ])
    live_card = ddk.Card(width=30,
                         style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
                         shadow_weight='heavy',
                         children=[ddk.Block(width=100,
                                             style={'margin':'0px'},
                                             children=dbc.ListGroup([
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                                                   active=True,
                                                                   action=True,
                                                                   children= ddk.Block(width=100,
                                                                                       children=[ddk.Block(width=20,
                                                                                                children=[html.P('Время')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('ПАРА')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Направление')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Цена')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Количество')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Стоимость')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center', 'max-width': '-webkit-fill-available',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),

                                                ]))
                                   ])
    hotbit_card = ddk.Card(width=30,
                         style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
                         shadow_weight='heavy',
                         children=[ddk.Block(width=100,
                                             style={'margin':'0px'},
                                             children=dbc.ListGroup([
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                                                   active=True,
                                                                   action=True,
                                                                   children= ddk.Block(width=100,
                                                                                       children=[ddk.Block(width=20,
                                                                                                children=[html.P('Время')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('ПАРА')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Направление')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Цена')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Количество')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('Стоимость')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center', 'max-width': '-webkit-fill-available',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),
                                                 dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},action=True,
                                                                   children=ddk.Block(width=100,
                                                                            children=[ddk.Block(width=20,
                                                                                                children=[html.P('08:54:40')]),
                                                                                      ddk.Block(width=20,
                                                                                                children=[html.P('USD/USDT')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('sell')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('0,99400000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,04100000')]),
                                                                                      ddk.Block(width=15,
                                                                                                children=[html.P('5,01075400')])])),

                                                ]))
                                   ])


    # create tab to enter a value
    first_tab = dcc.Tab(label="Ключи",
                        selected_style={'border': '2px solid #1f78b4'},
                        style={'background-color': '#ebeded'},
                        children=[ddk.Card(style={'width': '50%', 'margin':'5px','background-color': '#e4e7e7a6'},card_hover=True,
                                           children=ddk.Block(width=100,
                                                              style={'justify-content': 'center'},
                                                              children=[ddk.Block(width=20, children=html.H2('btc-Alpha',
                                                                                                             style={'text-align': 'center', 'justify':'center'})),
                                                                       ddk.Block(width=80, children=[ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="API key",
                                                                                                                                  style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'})),
                                                                                                     ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Secret API",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'}))]),
                                                                       ])),
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'},card_hover=True,
                                           children=ddk.Block(width=100,
                                                              style={'justify-content': 'center'},
                                                              children=[ddk.Block(width=20, children=html.H2('Livecoin',
                                                                                                             style={'text-align': 'center', 'justify':'center'})),
                                                                       ddk.Block(width=80, children=[ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="API key",
                                                                                                                                  style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'})),
                                                                                                     ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Secret API",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'}))]),
                                                                       ])),
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'},card_hover=True,
                                           children=ddk.Block(width=100,
                                                              style={'justify-content': 'center'},
                                                              children=[ddk.Block(width=20, children=html.H2('Hotbit',
                                                                                                             style={'text-align': 'center', 'justify':'center'})),
                                                                       ddk.Block(width=80, children=[ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="API key",
                                                                                                                                  style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'})),
                                                                                                     ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Secret API",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'}))]),
                                                                       ])),
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'}, card_hover=True,children=ddk.Block(width=100,
                                                                                                                       style={'justify-content': 'center'},
                                                             children=[ddk.Block(width=20, children=html.H2('TELEGRAM')),
                                                                       ddk.Block(width=80, children=[ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Chat id",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'})),
                                                                                                     ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Token",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'}))]),
                                                                       ])),
                                  ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                                           card_hover=True, children=ddk.Block(width=100,
                                                                               style={'justify-content': 'center'},
                                                                               children=[
                                                                                   ddk.Block(width=100,
                                                                                             children=[
                                                                                                 ddk.Block(width=20,
                                                                                                           children=html.H2(
                                                                                                               'Alpha Комиссия')),
                                                                                                 ddk.Block(width=20,
                                                                                                           children=[
                                                                                                            dcc.Input(
                                                                                                                id='Alpha_com',
                                                                                                 placeholder="1,002 = 0.2%",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                                                 ddk.Block(width=10,
                                                                                                           children=html.Button(
                                                                                                               'Submit',
                                                                                                               id='Alpha_btn')),
                                                                                                 ddk.Block(width=50,
                                                                                                           children=html.Div(id='output-alpha',
                                                                                                                             children=float(com['main']['alfa'])))
                                                                                         ]),
                                                                                   ddk.Block(width=100,
                                                                                             children=[
                                                                                                 ddk.Block(width=20,
                                                                                                           children=html.H2(
                                                                                                               'LiveCoin Комиссия')),
                                                                                                 ddk.Block(width=20,
                                                                                                           children=[
                                                                                                            dcc.Input(
                                                                                                                id='Live_com',
                                                                                                 placeholder=" 1,002 = 0.2% ",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                                                 ddk.Block(width=10,
                                                                                                           children=html.Button('Submit', id='LiveCoin_btn'),
                                                                                                           ),
                                                                                                 ddk.Block(width=50,
                                                                                                           children=html.Div(id='output-live',
                                                                                                                             children=float(com['main']['live'])))
                                                                                         ]),
                                                                                   ddk.Block(width=100,
                                                                                             children=[
                                                                                                 ddk.Block(width=20,
                                                                                                           children=html.H2(
                                                                                                               'HOTBIT Комиссия')),
                                                                                                 ddk.Block(width=20,
                                                                                                           children=[
                                                                                                            dcc.Input(
                                                                                                                id='Hot_com',
                                                                                                 placeholder="1,002 = 0.2%",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                                                 ddk.Block(width=10,
                                                                                                           children=html.Button(
                                                                                                               'Submit',
                                                                                                               id='Hot_btn')),
                                                                                                 ddk.Block(width=50,
                                                                                                           children=html.Div(id='output-hot',
                                                                                                                             children=float(com['main']['hot'])))
                                                                                         ]),




                                                                               ]))



                                  ])



    # create tab to retrieve the value entered in the other tab
    second_tab = dcc.Tab(label="Настройки",
                         style={'background-color': '#ebeded'},
                        selected_style={'border': '2px solid #1f78b4'},
                         children=ddk.Card(
                             shadow_weight='heavy',
                             children=[dbc.ListGroup(
                                 id="listcardreg",
                                 children=[i for i in group_of_regims()]),
                                 html.Button('Добавить Режим', id='New_Regim_btn')]))


    # create tab to retrieve the value entered in the other tab
    third_tab = dcc.Tab(label="Статистика",
                        selected_style={'border': '2px solid #1f78b4'},
                        style={'background-color': '#ebeded'},
                         children=[
                             ddk.Block(width=100, children=[alfa_card, live_card, hotbit_card]),
                             ddk.Card(children=[dash_table.DataTable(
                                 id="valuta",
                                 data=valuta.to_dict('records'),
                                 columns=[{'id': c, 'name': c} for c in valuta.columns],
                                 page_action='native',
                                 filter_action='native',
                                 filter_query='',
                                 sort_action='native',
                                 sort_mode='multi',
                                 sort_by=[],
                                 style_cell_conditional=[
                                     {
                                         'if': {'column_id': c},
                                         # 'pd.options.display.float_format': '{:.5f}'.format,
                                         'textAlign': 'center'
                                     } for c in ['SUMMA']
                                 ],
                                 style_data_conditional=[
                                     {
                                         'if': {'row_index': 'odd'},
                                         'backgroundColor': 'rgb(248, 248, 248)'
                                     }
                                 ],
                                 style_header={
                                     'backgroundColor': 'rgb(230, 230, 230)',
                                     'fontWeight': 'bold'
                                 }
                             ),
                             ]),
                             ddk.Card(children=[dash_table.DataTable(
                                                            id="table",
                                                            data=final.to_dict('records'),
                                                            columns=[{'id': c, 'name': c} for c in final.columns],
                                                            page_action='native',
                                                            filter_action='native',
                                                            filter_query='',
                                                            sort_action='native',
                                                            sort_mode='multi',
                                                            sort_by=[],
                                                            export_format='xlsx',
                                                            export_headers='display',
                                                            merge_duplicate_headers=True,
                                                            style_cell_conditional=[
                                                                # {'if': {'column_id': 'PROFIT'},
                                                                #  'pd.options.display.float_format': "'${:.2f}'.format",
                                                                #  'textAlign': 'center'},
                                                                # {'if': {'column_id': 'PERCENT'},
                                                                #  'pd.options.display.float_format': "'${:.2f}'.format",
                                                                #  'textAlign': 'center'},
                                                                # {'if': {'column_id': 'volume_x'},
                                                                #  'pd.options.display.float_format': "'${:.5f}'.format",
                                                                #  'textAlign': 'center'},
                                                                # {'if': {'column_id': 'volume_y'},
                                                                #  'pd.options.display.float_format': "'${:.5f}'.format",
                                                                #  'textAlign': 'center'},
                                                                # {'if': {'column_id': 'volume'},
                                                                #  'pd.options.display.float_format': "'${:.5f}'.format",
                                                                #  'textAlign': 'center'},





                                                                # [{
                                                                #     'if': {'column_id': c},
                                                                #     'pd.options.display.float_format':"'${:.2f}'.format",
                                                                #     'textAlign': 'center'
                                                                # } for c in ['PROFIT', 'PERCENT']],
                                                                # [{
                                                                #     'if': {'column_id': d},
                                                                #     'pd.options.display.float_format': "'${:.5f}'.format",
                                                                #     'textAlign': 'center'
                                                                # } for d in ['volume_x', 'volume_x', 'volume']]


                                                            ],
                                                            style_data_conditional=[
                                                                {
                                                                    'if': {'row_index': 'odd'},
                                                                    'backgroundColor': 'rgb(248, 248, 248)'
                                                                }
                                                            ],
                                                            style_header={
                                                                'backgroundColor': 'rgb(230, 230, 230)',
                                                                'fontWeight': 'bold'
                                                            }
                                                            ),
                             ])]
                        )


    # assemble tabs in dcc.Tabs object
    tabs = dcc.Tabs(children=[third_tab, second_tab, first_tab])
    # create layout
    layout = html.Div(children=[tabs, store_session_id_div, interval])

    return layout


layout_main = serve_layout()


