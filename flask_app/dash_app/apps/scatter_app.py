# This file contains the layout for the 'plot' page

import dash
import pandas as pd
from dash import html, Dash, Output, Input
from dash import dcc
import dash_bootstrap_components as dbc
from flask_app.dash_app.apps.data import Data
import warnings
from flask_app.dash_app.apps.create_charts import ScatterPlot

data = Data()
data.get_data()
data.df_initialise(data.df_initial)
data.create_lists(data.df_business)

df = pd.DataFrame()
for year in data.years:
    df = df.append(data.process_data(year, data.df_taxes, data.df_business))

scatter = ScatterPlot(df)
fig_scatter = scatter.create_plot()


class ScatterApp:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/scatter_app/',
                        suppress_callback_exceptions=True, server=flask_server, external_stylesheets=[dbc.themes.LUX],
                        meta_tags=[{
                            'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'
                        }])

    def setup(self):
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = html.Div(children=[
            html.H2(children='Ease of Doing Business vs Paying Taxes Ranking', style={'margin-left': '70px'}),

            html.Div(children='''
                The scatter plot gives each country's scores for paying taxes (x) and ease of doing business (y).
                Both indicators are scored out of 100, with a higher score indicating a more business-friendly environment.
                Different years can be compared using the slider at the bottom, or by playing the animation.
            ''', style={'margin-left': '70px'}),

            dcc.Graph(
                id='scatter-plot',
                figure=fig_scatter
            )
        ])
