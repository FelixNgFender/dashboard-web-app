import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Exploratory Data Analysis")

# Page 2 data
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
myDropdown1 = dcc.Dropdown(options=['Max cycle lifetime for all units', 'Distribution of maximum lifetime in cycles','Correlation matrix'],
                        value='Max cycle lifetime for all units')
myDropdown2 = dcc.Dropdown(options=[''.join(['Unit ', str(i)]) for i in range(1, 101)],
                        value='Unit 1')
myDropdown3 = dcc.Dropdown(options=['s1: Fan inlet temperature (◦R)',
                                    's2: LPC outlet temperature (◦R)',
                                    's3: HPC outlet temperature (◦R)',
                                    's4: LPT outlet temperature (◦R)',
                                    's5: Fan inlet Pressure (psia)',
                                    's6: bypass-duct pressure (psia)',
                                    's7: HPC outlet pressure (psia)',
                                    's8: Physical fan speed (rpm)',
                                    's9: Physical core speed (rpm)',
                                    's10: Engine pressure ratio (P50/P2)',
                                    's11: HPC outlet Static pressure (psia)',
                                    's12: Ratio of fuel flow to Ps30 (pps/psia)',
                                    's13: Corrected fan speed (rpm)',
                                    's14: Corrected core speed (rpm)',
                                    's15: Bypass Ratio',
                                    's16: Burner fuel-air ratio',
                                    's17: Bleed Enthalpy',
                                    's18: Required fan speed',
                                    's19: Required fan conversion speed',
                                    's20: High-pressure turbines Cool air flow',
                                    's21: Low-pressure turbines Cool air flow'],
                            value='s1: Fan inlet temperature (◦R)')
myGraph = dcc.Graph()

# Layout
layout = html.Div(
    [
        dbc.Row([
            dbc.Col([
                myDropdown1
            ], width=4),
            dbc.Col([
                myDropdown2
            ], width=4),
            dbc.Col([
                myDropdown3
            ], width=4)
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
    Input(myDropdown1, 'value'),
    Input(myDropdown2, 'value'),
    Input(myDropdown3, 'value')
)
def updateGraph(value1, value2, value3):
    if value1 == 'Max cycle lifetime for all units':
        fig = px.bar(max_time_cycles, x='cycle', orientation='h',
                    height=1000,
                    title='Max cycle lifetime for all units')
    elif value1 == 'Distribution of maximum lifetime in cycles':
        fig = px.histogram(max_time_cycles, x='cycle', marginal='box',
                    height=700, 
                    nbins=20,
                    title='Distribution of maximum lifetime in cycles')
    elif value1 == 'Correlation matrix':
        fig = px.imshow(corr, text_auto=True, height=1600, title='Correlation matrix')
        fig.update_xaxes(side="top")
    return fig