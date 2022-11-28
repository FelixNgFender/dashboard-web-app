import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__, path='/') # '/' is home page

# Layout
layout = html.Div(
    [
        dcc.Markdown(children='# Hello World')
    ]
)