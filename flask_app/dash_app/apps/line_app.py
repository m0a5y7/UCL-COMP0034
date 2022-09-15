# This file contains the layout for the 'line graph' page

import pandas as pd
from dash import html, Dash
from dash import dcc, Output, Input
import dash_bootstrap_components as dbc
from flask_app.dash_app.apps.scatter_app import df, data
from flask_app.dash_app.apps.create_charts import LineChart
from flask_app.dash_app.app import app

graph = LineChart(df)
line_graph = graph.create_chart('Afghanistan')
tax_growths = []
business_growths = []
for country in data.countries:
    df_country = df[df['country'] == country]
    tax_score_2020 = float(df_country.loc[df_country['year'] == '2020', 'tax_score'])
    tax_score_2016 = float(df_country.loc[df_country['year'] == '2016', 'tax_score'])
    if tax_score_2016 != 0:
        tax_growth = float("{:.2f}".format(((tax_score_2020-tax_score_2016)/tax_score_2016) * 100))
    else:
        tax_growth = 0
    tax_growths.append(tax_growth)
    b_score_2020 = float(df_country.loc[df_country['year'] == '2020', 'business_score'])
    b_score_2016 = float(df_country.loc[df_country['year'] == '2016', 'business_score'])
    if b_score_2016 != 0:
        b_growth = float("{:.2f}".format(((b_score_2020-b_score_2016)/b_score_2016) * 100))
    else:
        b_growth = 0
    business_growths.append(b_growth)

df_growth = pd.DataFrame()
df_growth = df_growth.assign(country=data.countries, tax_growth=tax_growths, business_growth=business_growths)


class LineApp:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/line_app/',
                        suppress_callback_exceptions=True, server=flask_server, external_stylesheets=[dbc.themes.LUX],
                        meta_tags=[{
                            'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'
                        }])

    def setup(self):
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = dbc.Container(fluid=True, children=[
            dbc.Row(
                dbc.Col(children=[html.Br(),
                                  html.H1('Paying Taxes and Ease of Doing Business'),
                                  ]),
            ),
            dbc.Row([
                dbc.Col(width=3, children=[
                    html.H4("Select Country"),
                    dcc.Dropdown(id='country-select',
                                 options=[{'label': x, 'value': x} for x in data.countries],
                                 value='Afghanistan'),
                    html.Br(),
                    html.Div(id='stats-card')
                ]),
                dbc.Col(width=9, children=[
                    dcc.Graph(id='line-graph', figure=line_graph)
                ])
            ])
        ])

    def setup_callbacks(self):
        @self.app.callback(Output("stats-card", "children"),
                           Output("line-graph", "figure"),
                           [Input("country-select", "value")])
        def render_output_panel(country_select):
            growth_df = df_growth[df_growth['country'] == country_select]
            card = dbc.Card(className="bg-dark text-light", children=[
                dbc.CardBody([
                    html.H4(country_select, id="card-name", className="card-title"),
                    html.Br(),
                    html.H6("Tax Score Growth since 2016:", className="card-title"),
                    html.H4("{:.2f}%".format(float(growth_df.tax_growth)), className="card-text text-light"),
                    html.Br(),
                    html.H6("Ease of Doing Business Growth since 2016:", className="card-title"),
                    html.H4("{:.2f}%".format(float(growth_df.business_growth)), className="card-text text-light")
                ])
            ])
            line_graph1 = graph.create_chart(country_select)
            return card, line_graph1
