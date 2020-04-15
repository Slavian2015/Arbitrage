from dash.dependencies import Input, Output, State
from app import dash_app, dash_db
import VILKA
from dash.exceptions import PreventUpdate
from dash_database import DashDatabase
import dash
import os
import json

dash_app.config['suppress_callback_exceptions'] = True



# putting your callbacks in functions is a nice trick to be able to move them in other modules and import them
def create_callback_save_value(app: dash.Dash,
                               dash_db: DashDatabase):
    @app.callback(Output('success_value_saved', 'children'),
                  [Input('ok_button', 'n_clicks')],  # the button triggers the callback
                  [State('input_div', 'value'),  # additional info that does not trigger the callback
                   State('session_id_div_id', 'data')])  # used to identify the user and save its data
    def save_value(n_clicks, value, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is None at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        dash_db.store_user_value(user_id=session_id,
                                 key_name='value',
                                 value=value)

        # return success message
        return "Your value was sucessfully saved. Try to retrieve it in the other tab now :)!"
def create_callback_retrieve_value(app: dash.Dash,
                                   dash_db: DashDatabase):
    @app.callback(Output('show_value_div', 'children'),
                  [Input('show_value_button', 'n_clicks')],
                  [State('session_id_div_id', 'data')])
    def retrieve_value(n_clicks, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is 0 at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        value = dash_db.get_user_value(user_id=session_id,
                                       key_name='value')

        # return success message
        return f"Your value is {value}"

def refresh(app: dash.Dash):

    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback(Output('table', 'data'), [Input('interval', 'n_intervals')])
    def trigger_by_modify(n):
        print ("###############  UPDATE   #########################")
        df10 = VILKA.restart()
        df10['id'] = df10.index
        return df10.to_dict('records')


def commis(app: dash.Dash):
    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-alpha', 'children'),
        [dash.dependencies.Input('Alpha_btn', 'n_clicks')],
        [dash.dependencies.State('Alpha_com', 'value')])
    def update_Alpha(n_clicks, value):
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["alfa"] = value

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-live', 'children'),
        [dash.dependencies.Input('Live_btn', 'n_clicks')],
        [dash.dependencies.State('Live_com', 'value')])
    def update_Alpha(n_clicks, value):
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["live"] = value

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-hot', 'children'),
        [dash.dependencies.Input('Hot_btn', 'n_clicks')],
        [dash.dependencies.State('Hot_com', 'value')])
    def update_Alpha(n_clicks, value):
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["hot"] = value

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

create_callback_save_value(dash_app, dash_db)
create_callback_retrieve_value(dash_app, dash_db)
refresh(dash_app)
commis(dash_app)

