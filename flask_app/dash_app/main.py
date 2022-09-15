# Run this file to create web page

from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output
from app import app
from flask_app.dash_app.apps import scatter_app, line_app
from flask_app.dash_app.apps import table_app, choropleth_app

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Scatter Plot", href="/plot"), id="app-1-link"),
        dbc.NavItem(dbc.NavLink("Maps", href="/maps"), id="app-2-link"),
        dbc.NavItem(dbc.NavLink("Line Graph", href="/graph"), id="app-3-link"),
        dbc.NavItem(dbc.NavLink("Ranking Table", href="/table"), id="app-4-link")
    ],
    brand="Business Viability by Country",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
])

index_layout = html.Div([
    html.H2(children='Page contents per tab', style={'margin-left': '70px'}),
    html.H3(children='Scatter plot: An animated scatterplot of indicators compared to each other',
            style={'margin-left': '70px'}),
    html.H3(children='Maps: An animated choropleth map visualisation of indicators', style={'margin-left': '70px'}),
    html.H3(children='Line graph: Visualisation of growth per country', style={'margin-left': '70px'}),
    html.H3(children='Ranking table: Top 10 countries for indicators and growth', style={'margin-left': '70px'}),
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/maps':
        return choropleth_app.app.layout
    elif pathname == '/plot':
        return scatter_app.app.layout
    elif pathname == '/table':
        return table_app.app.layout
    elif pathname == '/graph':
        return line_app.layout
    elif pathname == '/':
        return index_layout
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True)
