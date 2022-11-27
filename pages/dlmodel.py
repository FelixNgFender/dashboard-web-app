import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Deep Learning Model") 

# Build the components

layout = html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/model_accuracy.png',
                            height='750px')
                ]
            ),
            dbc.Col(
                [
                    html.Img(src='assets/model_loss.png',
                            height='750px')
                ]
            )
        ], justify='between'),
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/model_mae.png',
                            height='750px')
                ]
            ),
            dbc.Col(
                [
                    html.Img(src='assets/model_r2.png',
                            height='750px')
                ]
            )
        ], justify='between'),
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/model_regression_loss.png',
                            height='750px')
                ]
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/model_verify.png',
                            height='375px')
                ]
            ),
            dbc.Col(
                [
                    html.Img(src='assets/model_regression_verify.png',
                            height='375px')
                ]
            )
        ], justify='between')
    ]
)