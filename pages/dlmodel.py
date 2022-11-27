import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

dash.register_page(__name__) 

# Page 1 data
df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Dropdown([x for x in df.continent.unique()], id='cont-choice', style={'width':'50%'}),
        dcc.Graph(id='line-fig',
                  figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
    ]
)