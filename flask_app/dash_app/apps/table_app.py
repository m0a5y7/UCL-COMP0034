# This file contains the layout for the 'tables' page

import dash
from dash import html, Dash
from dash import dash_table
import dash_bootstrap_components as dbc
from flask_app.dash_app.apps.scatter_app import df
import warnings
from flask_app.dash_app.apps.create_charts import RankTable
from flask_app.dash_app.apps.line_app import df_growth

warnings.simplefilter(action='ignore', category=FutureWarning)

table = RankTable(df)
gtable = RankTable(df_growth)

tax_r = table.create_table("tax_score", "2020")
bus_r = table.create_table("business_score", "2020")
tax_r = tax_r.drop("business_score", axis=1)
bus_r = bus_r.drop("tax_score", axis=1)

tax_gr = gtable.growth_table("tax_growth")
bus_gr = gtable.growth_table("business_growth")
tax_gr = tax_gr.drop("business_growth", axis=1)
bus_gr = bus_gr.drop("tax_growth", axis=1)


class TableApp:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/table_app/',
                        suppress_callback_exceptions=True, server=flask_server, external_stylesheets=[dbc.themes.LUX],
                        meta_tags=[{
                            'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'
                        }])

    def setup(self):
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = html.Div(children=[
            html.H2(children='Top 10 countries in 2020 per indicator',
                    style={'margin-left': '70px'}
                    ),

            dbc.Container([
                 dbc.Label('Ease of doing business'),
                 dash_table.DataTable(bus_r.to_dict('records'), [{"name": i, "id": i} for i in bus_r.columns])
             ]),

            dbc.Container([
                 dbc.Label('Paying taxes'),
                 dash_table.DataTable(tax_r.to_dict('records'), [{"name": i, "id": i} for i in tax_r.columns])
             ]),

            html.H2(children='Top 10 growth per indicator',
                    style={'margin-left': '70px'}
                    ),

            dbc.Container([
                 dbc.Label('Growth in tax score since 2016 (%)'),
                 dash_table.DataTable(tax_gr.to_dict('records'), [{"name": i, "id": i} for i in tax_gr.columns])
             ]),

            dbc.Container([
                 dbc.Label('Growth in ease of doing business score since 2016 (%)'),
                 dash_table.DataTable(bus_gr.to_dict('records'), [{"name": i, "id": i} for i in bus_gr.columns])
             ]),
        ])
