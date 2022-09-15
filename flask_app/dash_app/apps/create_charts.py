# This file contains classes to create charts

import plotly.express as px
import plotly.graph_objects as go


class ChoroplethMaps:
    def __init__(self, data, geojson):
        self.data = data
        self.geojson = geojson

    def create_map(self, indicator, title):
        data = self.data
        geojson = self.geojson
        figure = px.choropleth(data, featureidkey='properties.ISO_A3', geojson=geojson, locations='code',
                               color=indicator, animation_frame='year', animation_group='country',
                               height=1000, width=1500, title=title)
        return figure


class ScatterPlot:
    def __init__(self, data):
        self.data = data

    def create_plot(self):
        data = self.data
        figure = px.scatter(data, x='tax_score', y='business_score', animation_frame='year', animation_group='country',
                            labels={'tax_score': 'Tax Score', 'business_score': 'Ease of Doing Business Score'},
                            hover_name='country', color='country', height=1000, range_x=[0, 100], range_y=[0, 100],
                            title='Paying Taxes Score vs Ease of Doing Business Score over time')
        return figure


class LineChart:
    def __init__(self, data):
        self.data = data

    def create_chart(self, country):
        data = self.data[self.data['country'] == country]
        taxes = go.Scatter(x=data['year'], y=data['tax_score'], mode='lines', name='Tax Scores',
                           line=dict(color='red', width=4))
        business = go.Scatter(x=data['year'], y=data['business_score'], mode='lines', name='Business Scores',
                              line=dict(color='blue', width=4))
        layout = go.Layout(showlegend=True, plot_bgcolor="#ffffff")
        figure = go.Figure(layout=layout)

        figure.add_trace(taxes)
        figure.add_trace(business)

        figure.update_layout(yaxis_title="Score")
        figure.update_yaxes(title_font=dict(size=14, color='#CDCDCD'),
                            tickfont=dict(color='#CDCDCD', size=12),
                            showgrid=True, gridwidth=1, gridcolor='#CDCDCD',
                            tick0=0.0, dtick=10.0)
        figure.update_xaxes(tickangle=90, tickfont=dict(color='#CDCDCD', size=12),
                            showline=True, linewidth=2, linecolor='#CDCDCD')

        return figure


class RankTable:
    def __init__(self, data):
        self.data = data

    def create_table(self, indicator, year):
        data = self.data
        df = data[data['year'] == year]
        df = df.assign(ranking=df[indicator].rank(ascending=0))
        df = df.set_index('ranking')
        df = df.sort_index()
        df = df.iloc[:10]
        return df

    def growth_table(self, indicator):
        data = self.data
        data = data.assign(ranking=data[indicator].rank(ascending=0))
        data = data.set_index("ranking")
        data = data.sort_index()
        data = data.iloc[:10]
        return data
