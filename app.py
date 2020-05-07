import dash
import dash_bootstrap_components as dbc
from dash_database import DashDatabase
import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = flask.Flask(__name__)
dash_app = dash.Dash(__name__,url_base_pathname="/", server=app,external_stylesheets=external_stylesheets)
dash_app.title = 'Best Arbitrage'
# dash_app.layout = serve_layout
dash_db = DashDatabase()  # create a DashDatabase instance for managing user values

