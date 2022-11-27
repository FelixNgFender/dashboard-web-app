import dash                             # pip install dash
from dash import html, dcc              
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

# Build your components
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
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