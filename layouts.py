import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app

###########  Main Page   ################

def serve_layout():
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
    first_tab = dcc.Tab(label="Enter a value",
                        children=[dcc.Input(placeholder="Enter value here", id="input_div"),
                                  html.Button(children="OK", id="ok_button"),
                                  dcc.Markdown(id="success_value_saved")])

    # create tab to retrieve the value entered in the other tab
    second_tab = dcc.Tab(label="Retrieve the value",
                         children=[html.Button(children="Show me the value", id="show_value_button"),
                                   dcc.Markdown(id="show_value_div")])

    # assemble tabs in dcc.Tabs object
    tabs = dcc.Tabs(children=[first_tab, second_tab])

    # create layout
    layout = html.Div(children=[tabs, store_session_id_div])

    return layout
layout_main = serve_layout()



