
import dash                             # pip install dash
from dash import html, dcc              
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/api')
# def get_incomes():
#     print('liem lon')
#     return '', 205


@app.route('/api/posts', methods=['POST'])
def post_api():
    if request.method == 'POST':
        data = request.get_json()
        # Code to process the received data and store it in the database
        return jsonify({"message": "Post created successfully"})

# Build your components
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB], server=app)
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Schneider Data Analytics",
                         style={'fontSize':50, 'textAlign':'center'}))
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)

# Deploy with dash-tools
# pip install dash-tools