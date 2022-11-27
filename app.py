import dash                             # pip install dash
from dash import html, dcc              
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

# Build your components
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Customize your own Layout
app.layout = html.Div(
    [
        # Framework of the main app
        html.Div("Schneider Data Analytics", style={'fontSize': 50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(children=page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ], style={'fontSize': 40, 'textAlign':'center'}),
        html.Hr(),

        # Content of each page
        dash.page_container
    ]
)

# # Callback allows components to interact
# @app.callback(
#     Output(myText, component_property='children'),
#     Output(myText, component_property='style'),
#     Input(myInput, component_property='value'),
#     Input(myRadio, component_property='value')
# )
# def update_title(user_input, radio_input):  # function arguments come from the component property of the Input
#     return user_input, {'color':radio_input}  # returned objects are assigned to the component property of the Output

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)

# Deploy with dash-tools
# pip install dash-tools