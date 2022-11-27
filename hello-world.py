from dash import Dash, dcc, Output, Input    # pip install dash
import dash_bootstrap_components as dbc      # pip install dash_bootstrap_components
import plotly.express as px                  # pip install plotly
import pandas as pd                          # pip install pandas

# Incorporate data into web app
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv")
print(df.head())

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
myTitle = dcc.Markdown(children='')
myGraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Cesarean Delivery Rate',  # initial value displayed when page first loads
                        clearable=False)


# Customize layout
    # Put the component inside the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([myTitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([myGraph], width=12)
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),

], fluid=True)

# Callbacks allow components to interact
# Callbacks are built from a callback decorator
# and a callback function
@app.callback(
    Output(myGraph, 'figure'),
    Output(myTitle, 'children'),
    Input(dropdown, 'value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input
    print(column_name)
    print(type(column_name))
    # https://plotly.com/python/choropleth-maps/
    fig = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        color=column_name,
                        animation_frame='YEAR')
    return fig, '# '+ column_name  # returned objects are assigned to the component property of the Output


# Run app
if __name__ == '__main__':
    app.run_server(port=8054)

# Deploy with dash-tools
# pip install dash-tools