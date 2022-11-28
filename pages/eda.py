import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Exploratory Data Analysis")

# page 2 data
df = pd.read_csv('data/PM_train.txt', sep=" ", header=None)
df.drop(df.columns[[26, 27]], axis=1, inplace=True)
df.columns = ['id', 'cycle', 'setting1', 'setting2', 'setting3', 's1', 's2', 's3',
                     's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
                     's15', 's16', 's17', 's18', 's19', 's20', 's21']

df = df.sort_values(['id','cycle'])

max_time_cycles = df[['id', 'cycle']].groupby('id').max()

# Data Labeling - generate column RUL(Remaining Useful Life or Time to Failure)
rul = pd.DataFrame(df.groupby('id')['cycle'].max()).reset_index()
rul.columns = ['id', 'max']
df = df.merge(rul, on=['id'], how='left')
df['RUL'] = df['max'] - df['cycle']
df.drop('max', axis=1, inplace=True)

# Compute the correlation matrix
corr = df.corr()

# Build components
myDropdown = dcc.Dropdown(options=['Max cycle lifetime for each unit', 'Distribution of maximum lifetime in cycles','Correlation matrix'],
                        value='Max cycle lifetime for each unit')
myGraph = dcc.Graph()

# Layout
layout = html.Div(
    [
        dbc.Row([
            dbc.Col([
                myDropdown
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                myGraph
            ], width=12)
        ])
    ]
)

# Callback
@callback(
    Output(myGraph, 'figure'),
    Input(myDropdown, 'value')
)
def updateGraph(value):
    if value == 'Max cycle lifetime for each unit':
        fig = px.bar(max_time_cycles, x='cycle', orientation='h',
                    height=1000,
                    title='Max cycle lifetime for each unit')
    elif value == 'Distribution of maximum lifetime in cycles':
        fig = px.histogram(max_time_cycles, x='cycle', marginal='box',
                    height=700, 
                    nbins=20,
                    title='Distribution of maximum lifetime in cycles')
    elif value == 'Correlation matrix':
        fig = px.imshow(corr, text_auto=True, height=1600, title='Correlation matrix')
        fig.update_xaxes(side="top")
    return fig