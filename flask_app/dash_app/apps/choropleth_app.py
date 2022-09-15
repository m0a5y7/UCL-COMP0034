# This file contains the layout for the 'maps' page

import dash
from dash import html, Dash, Output, Input
from dash import dcc
import dash_bootstrap_components as dbc
from flask_app.dash_app.apps.scatter_app import df, data
from flask_app.dash_app.apps.create_charts import ChoroplethMaps


map1 = ChoroplethMaps(df, data.geojson)

taxes_map = map1.create_map('tax_score', 'Choropleth Map of Tax Scores over time')
business_map = map1.create_map('business_score', 'Choropleth Map of Ease of Doing Business Score over time')

class ChoroplethApp:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/choropleth_app/',
                        suppress_callback_exceptions=True, server=flask_server, external_stylesheets=[dbc.themes.LUX],
                        meta_tags=[{
                            'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'
                        }])

    def setup(self):
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = html.Div(children=[
            html.H2(children='Choropleth Maps of Paying Taxes Score and Doing Business Score by country from 2016 to 2020',
                    style={'margin-left': '70px'}
                    ),

            html.Div(children='''
            The choropleth maps below visualise how every country performs in each business indicator.
            Different years can be compared using the slider at the bottom, or by playing the animation.
            ''', style={'margin-left': '70px'}),

            dcc.Graph(
                id='choropleth-map-1',
                figure=taxes_map
            ),

            dcc.Graph(
                id='choropleth-map-2',
                figure=business_map
            )
        ])

