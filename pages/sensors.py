import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Sensor Installation Guide")

# Layout
layout = html.Div(
    [
        dcc.Markdown(children="# Hello World")
    ]
)