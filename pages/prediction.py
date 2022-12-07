import dash
from dash import dcc, html, callback
import pickle

dash.register_page(__name__, name="Predictive Maintenance Rating")

# Load the weights from the pickle file
model = pickle.load(open('model/myData.pkl', 'rb'))

# Create the app layout
layout = html.Div([

    html.Div(["Inputs:"], style={'fontSize': 18}),

    html.Div([
        html.Div([
            dcc.Input(id="input_1", type='number', min=0, max=2, step=1, placeholder="Type")
        ], className="three columns"),

        html.Div([
            dcc.Input(id="input_2", type="number", min=273, placeholder="Air temperature [K]")
        ], className="three columns"),

        html.Div([
            dcc.Input(id="input_3", type="number", min=273, placeholder="Process temperature [K]")
        ], className="three columns"),

        html.Div([
            dcc.Input(id="input_4", type="number", min=0, placeholder="Rotational speed [rpm]")
        ], className="three columns"),

        html.Div([
            dcc.Input(id="input_5", type="number", min=0, placeholder="Torque [Nm]")
        ], className="three columns"),

        html.Div([
            dcc.Input(id="input_6", type="number", min=0, step=1, placeholder="Tool wear [min]")
        ], className="three columns")
    ], className="row"),

    html.Br(),

    html.Button('Submit', id='button'),

    html.Div(id='output_div', children='')

])

@callback(
    dash.dependencies.Output('output_div', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input_1', 'value'),
    dash.dependencies.State('input_2', 'value'),
    dash.dependencies.State('input_3', 'value'),
    dash.dependencies.State('input_4', 'value'),
    dash.dependencies.State('input_5', 'value'),
    dash.dependencies.State('input_6', 'value')])
def update_output(n_clicks, input1, input2, input3, input4, input5, input6):
    inputs = [input1, input2, input3, input4, input5, input6]
    pred = model.predict([inputs])
    return f"The prediction is: {pred[0]}"
