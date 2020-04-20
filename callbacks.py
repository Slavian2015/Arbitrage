from dash.dependencies import Input, Output, State, ALL, MATCH
from app import dash_app, dash_db
import VILKA
from dash.exceptions import PreventUpdate
from dash_database import DashDatabase
import dash
import os
import json
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import layouts
import pandas as pd

dash_app.config['suppress_callback_exceptions'] = True
main_path_data = os.path.abspath("./data")


# putting your callbacks in functions is a nice trick to be able to move them in other modules and import them
def create_callback_save_value(app: dash.Dash, dash_db: DashDatabase):
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

def create_callback_retrieve_value(app: dash.Dash, dash_db: DashDatabase):
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
        df = VILKA.restart()
        df10 = df[0]
        print("DF10  SHAPE   :",  df10.shape[0])
        if df10.shape[0]>0:
            return df10.to_dict('records')
        else:
            my_col=['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y', 'volume_x',
                 'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']
            df10 = pd.DataFrame(columns=my_col)
            return df10.to_dict('records')


def commis(app: dash.Dash):
    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-alpha', 'children'),
        [dash.dependencies.Input('Alpha_btn', 'n_clicks')],
        [dash.dependencies.State('Alpha_com', 'value')])
    def update_Alpha(n_clicks, value):
        if n_clicks is None:
            raise PreventUpdate

        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["alfa"] = float(value)

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
        if n_clicks is None:
            raise PreventUpdate
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["live"] = float(value)

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
        if n_clicks is None:
            raise PreventUpdate
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["hot"] = float(value)

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

def creat_reg(app: dash.Dash):

    @app.callback(
        dash.dependencies.Output('listcardreg', 'children'),
        [dash.dependencies.Input('New_Regim_btn', 'n_clicks'),
         Input('interval', 'n_intervals')])

    def create(n_clicks, n):

        if n_clicks is None or n is None:
            raise PreventUpdate

        elif n_clicks > 0:
            with open(main_path_data + "\\regim.json", "r") as file:
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)
                next_id = str(int(param[-1]) + 1)
                data[next_id] = {"option": "off", "val1": "", "val2": "", "val3": "", "birga1": "", "birga2": "",
                                 "profit": "",
                                 "order": "", "per": ""}
                f = open(main_path_data + "\\regim.json", "w")
                json.dump(data, f)
                # print("BEFORE2 :", data)
                f.close()
            list_group = [i for i in layouts.group_of_regims()]
            return list_group

        else:
            list_group = [i for i in layouts.group_of_regims()]
            return list_group


def save_reg_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'option', 'index': MATCH}, 'children')],
       [Input({'type': 'checklist', 'index': MATCH}, 'value')],
        [State({'type': 'checklist', 'index': MATCH}, 'id'),

         State({'type': 'val1', 'index': MATCH}, "value"),
         State({'type': 'val2', 'index': MATCH}, "value"),
         State({'type': 'val3', 'index': MATCH}, "value"),
         State({'type': 'birga1', 'index': MATCH}, "value"),
         State({'type': 'birga2', 'index': MATCH}, "value"),

         State({'type': 'profit', 'index': MATCH}, "value"),
         State({'type': 'order', 'index': MATCH}, "value"),
         State({'type': 'percent', 'index': MATCH}, "value"),
         ]
    )
    def display_output(value,id, val1, val2, val3, birga1, birga2, profit, order, percent):
        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            pass

        if order is None:
            order = ""
        else:
            order = float(order)

        if percent is None:
            percent = ""
        else:
            percent = percent

        print(id['index'])



        if not value:
            # Change "option" in Regim

            print("#########     OFF    ##############")



            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            print("  REGIM JSON :", '\n', json_object)


            json_object[id['index']]['option'] = "OFF"

            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return ["{}".format(json_object[id['index']]['option'])]

        else:

            print ("#########     ON    ##############")

            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            print("  REGIM JSON :", '\n', json_object)


            json_object[id['index']]['option'] = "active"
            json_object[id['index']]['val1'] = val1
            json_object[id['index']]['val2'] = val2
            json_object[id['index']]['val3'] = val3
            json_object[id['index']]['birga1'] = birga1
            json_object[id['index']]['birga2'] = birga2
            json_object[id['index']]['profit'] = float(profit)
            json_object[id['index']]['order'] = order
            json_object[id['index']]['per'] = percent

            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return ["{}".format(json_object[id['index']]['option'])]







create_callback_save_value(dash_app, dash_db)
create_callback_retrieve_value(dash_app, dash_db)
refresh(dash_app)
commis(dash_app)
creat_reg(dash_app)
save_reg_data(dash_app)
