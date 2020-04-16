from app import dash_app, app
from layouts import layout_main
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

# git push heroku master
import callbacks


dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
                     children=[
                         ddk.Block(width=100,
                                   style={'height': '100vh', 'width': '100%', 'text-align':'center', 'padding':'0'},
                                   children=ddk.Block(width=100,
                                                      style={'margin': '0', 'width':'100%'},
                                                      children=html.Div(id='page-content')))

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