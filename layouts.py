import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import pandas as pd
import dash_table
import os
from app import dash_app

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



def serve_layout():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


    param_head = ddk.Card(style={'width': '100%', 'line-height': '1', 'height': '70px', 'margin': '0', 'max-height': 'fit-content', 'background-color': '#fff'},
                          children=ddk.Block(width=100,
                                             style={'justify-content': 'center'},
                                             children=[ddk.Block(width=5, style={'vertical-align': '-webkit-baseline-middle'},children=html.H2('Active',
                                                                                           style={'margin': '0',
                                                                                               'text-align': 'center',
                                                                                               'justify': 'center'})),
                                                       ddk.Block(width=45, style={'vertical-align': '-webkit-baseline-middle'},children=[
                                                           ddk.Block(width=33, children=html.H2('btc-Alpha',
                                                                                                style={'margin': '0',
                                                                                                    'text-align': 'center',
                                                                                                    'justify': 'center'})),
                                                           ddk.Block(width=33, children=html.H2('Livecoin',
                                                                                                style={'margin': '0',
                                                                                                    'text-align': 'center',
                                                                                                    'justify': 'center'})),
                                                           ddk.Block(width=33, children=html.H2('Hotbit',
                                                                                                style={'margin': '0',
                                                                                                    'text-align': 'center',
                                                                                                    'justify': 'center'}))]),
                                                       ddk.Block(width=45, style={'vertical-align': '-webkit-baseline-middle'},children=html.H2('PARAMETERS',
                                                                                            style={'margin': '0',
                                                                                                'text-align': 'center',
                                                                                                'justify': 'center'})),
                                                       ddk.Block(width=5, style={'vertical-align': '-webkit-baseline-middle'},children=html.H2('Signal (on/off)',
                                                                                           style={'margin': '0',
                                                                                               'text-align': 'center',
                                                                                               'justify': 'center'}))]))

    param_val = ddk.Card(style={'width': '100%', 'margin': '0', 'background-color': '#e4e7e7a6'},
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center','vertical-align': '-webkit-baseline-middle',},
                                            children=[ddk.Block(width=5, style={'vertical-align': '-webkit-baseline-middle'}, children=html.H2('Active',
                                                                                          style={'margin': '0',
                                                                                                 'text-align': 'center',
                                                                                                 'vertical-align': '-webkit-baseline-middle',
                                                                                                 'justify-content': 'center'})),
                                                      ddk.Block(width=45,
                                                                children=[ddk.Block(width=33, style={'vertical-align': '-webkit-baseline-middle'}, children=[
                                                                    ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown( style={'background-color': '#fff'},
                                                                        options=[
                                                                            {'label': 'BTC', 'value': 'BTC'},
                                                                            {'label': 'USD', 'value': 'USD'},
                                                                            {'label': 'USDt', 'value': 'USDt'},
                                                                            {'label': 'ETH', 'value': 'ETH'}
                                                                        ],
                                                                        value='BTC')),
                                                                    ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown(style={'background-color': '#fff'},
                                                                        options=[
                                                                            {'label': 'BTC', 'value': 'BTC'},
                                                                            {'label': 'USD', 'value': 'USD'},
                                                                            {'label': 'USDt', 'value': 'USDt'},
                                                                            {'label': 'ETH', 'value': 'ETH'}
                                                                        ],
                                                                        value='USDt'))]),
                                                                          ddk.Block(width=33, style={'vertical-align': '-webkit-baseline-middle'},children=[
                                                                              ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown(style={'background-color': '#fff'},
                                                                                  options=[
                                                                                      {'label': 'BTC', 'value': 'BTC'},
                                                                                      {'label': 'USD', 'value': 'USD'},
                                                                                      {'label': 'USDt','value': 'USDt'},
                                                                                      {'label': 'ETH','value': 'ETH'}
                                                                                  ],
                                                                                  value='BTC')),
                                                                              ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown(style={'background-color': '#fff'},
                                                                                  options=[
                                                                                      {'label': 'BTC', 'value': 'BTC'},
                                                                                      {'label': 'USD', 'value': 'USD'},
                                                                                      {'label': 'USDt','value': 'USDt'},
                                                                                      {'label': 'ETH','value': 'ETH'}
                                                                                  ],
                                                                                  value='USDt'))]),
                                                                          ddk.Block(width=33, style={'vertical-align': '-webkit-baseline-middle'},children=[
                                                                              ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown(style={'background-color': '#fff'},
                                                                                  options=[
                                                                                      {'label': 'BTC', 'value': 'BTC'},
                                                                                      {'label': 'USD', 'value': 'USD'},
                                                                                      {'label': 'USDt','value': 'USDt'},
                                                                                      {'label': 'ETH','value': 'ETH'}
                                                                                  ],
                                                                                  value='BTC')),
                                                                              ddk.Block(width=100, style={'width':'80%', 'margin': '2px'}, children=dcc.Dropdown(style={'background-color': '#fff'},
                                                                                  options=[
                                                                                      {'label': 'BTC', 'value': 'BTC'},
                                                                                      {'label': 'USD', 'value': 'USD'},
                                                                                      {'label': 'USDt','value': 'USDt'},
                                                                                      {'label': 'ETH ','value': 'ETH'}
                                                                                  ],
                                                                                  value='USDt'))])
                                                                          ]),

                                                      ddk.Block(width=45, style={'vertical-align': '-webkit-baseline-middle'},children=[ddk.Block(width=100,
                                                                                              children=[
                                                                                                  ddk.Block(width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                            children=[
                                                                                                                ddk.Block(
                                                                                                                    width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                                    children=[
                                                                                                                        html.P(
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
                                                                                                                                'max-width': '60px'})])]
                                                                                                            ),
                                                                                                  ddk.Block(width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                            children=[
                                                                                                                ddk.Block(
                                                                                                                    width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                                    children=[
                                                                                                                        html.P(
                                                                                                                            '$ profit',
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
                                                                                                                                'max-width': '60px'})])]
                                                                                                            )]
                                                                                              ),
                                                                                    ddk.Block(width=100,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                              children=[
                                                                                                  ddk.Block(width=50,
                                                                                                            children=[
                                                                                                                ddk.Block(
                                                                                                                    width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                                    children=[
                                                                                                                        html.P(
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
                                                                                                                                'max-width': '60px'})])]
                                                                                                            ),
                                                                                                  ddk.Block(width=50,
                                                                                                            children=[
                                                                                                                ddk.Block(
                                                                                                                    width=50,style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                                    children=[
                                                                                                                        html.P(
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
                                                                                                                                'max-width': '60px'})])]
                                                                                                            )]
                                                                                              )]
                                                                ),

                                                      ddk.Block(width=5,
                                                                style={'vertical-align': '-webkit-baseline-middle'},
                                                                children=dbc.Checklist(style={'text-align': 'center',
                                                                                              'border': '#333',
                                                                                              'vertical-align': '-webkit-baseline-middle',
                                                                                              'justify-content': 'center'},
                                                                                       options=[
                                                                                           {"label": "Off",
                                                                                            "value": 1}
                                                                                       ],
                                                                                       value=[],
                                                                                       id="checklist-inline-input",
                                                                                       inline=True))
                                                      ]))








    """Creates the layout for each user of the app.
    This function is executed each time a session is created for the app.
    It creates a new session id (a uuid.uuid1 as string) each time.

    This session id will be used in combination with a DashDatabase instance to manage user values.
    It will be fetched via the property data of a dcc.Store component.
    """

    # create a session id
    session_id = str(uuid.uuid1())
    # store the session id in a dcc.Store component (invisible component for storing data)
    store_session_id_div = dcc.Store(id='session_id_div_id',
                                     storage_type='session',  # IMPORTANT! see docstring of dcc.Store
                                     data=session_id)





    # create tab to enter a value
    first_tab = dcc.Tab(label="Ключи",
                        children=[ddk.Card(style={'width': '50%', 'margin':'5px','background-color': '#e4e7e7a6'},
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
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'},
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
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'},
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
                                  ddk.Card(style={'width': '50%', 'margin':'5px', 'background-color': '#e4e7e7a6'}, children=ddk.Block(width=100,
                                                                                                                       style={'justify-content': 'center'},
                                                             children=[ddk.Block(width=20, children=html.H2('TELEGRAM')),
                                                                       ddk.Block(width=80, children=[ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Chat id",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'})),
                                                                                                     ddk.Block(width=100,
                                                                                                               children=dcc.Input(placeholder="Token",style={'border':'double', 'margin':'0', 'background-color': 'ivory', 'width': '-webkit-fill-available'}))]),
                                                                       ]))



                                  ])



    # create tab to retrieve the value entered in the other tab
    second_tab = dcc.Tab(label="Настройки",
                         children=ddk.Card(children=
                                        dbc.ListGroup([
                                            dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'height': '70px', 'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                                              children=param_head),
                                            dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'height': 'fit-content', 'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                                              children=param_val),
                                            dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
               'height': 'fit-content', 'justify-content': 'center',
               'vertical-align': '-webkit-baseline-middle',
               'max-height': 'fit-content', 'padding': '0px',
               'list-style': 'none',
               'align-items': 'center'},
                                                              children=param_val),
                                                ])))


    # create tab to retrieve the value entered in the other tab
    third_tab = dcc.Tab(label="Статистика",
                         children=ddk.Card(children=dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
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
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
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
    )))


    # assemble tabs in dcc.Tabs object
    tabs = dcc.Tabs(children=[third_tab, second_tab, first_tab])
    # create layout
    layout = html.Div(children=[tabs, store_session_id_div])

    return layout
layout_main = serve_layout()


