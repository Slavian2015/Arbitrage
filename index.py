from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

from app import dash_app, app
from layouts import layout_main
import callbacks


dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
                     children=[
                         ddk.Header(style={'height': '7vh', 'background-color': '#1f78b494', 'opacity': '1'},
                                    children=[
                                        ddk.Logo(src='../assets/favicon.ico'),
                                        ddk.Block(style={'text-align': 'right'}, children=[])]),

                         ddk.Block(width=100,
                                   style={'height': '90vh', 'text-align':'center', 'overflowY':'scroll', 'padding':'10px'},
                                   children=html.Div(id='page-content'))






])])




@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return layout_main
    else:
        return '404'

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=False)