# This file contains code to sort and process data to be used in the app

from pathlib import Path

import pandas as pd
import json


class Data:
    def __init__(self):
        self.df_initial = pd.DataFrame()
        self.countries = []
        self.country_codes = []
        self.years = []
        self.df_taxes = pd.DataFrame()
        self.df_business = pd.DataFrame()
        self.df_final = pd.DataFrame()
        self.tax_scores = []
        self.business_scores = []
        self.geojson = []

    def get_data(self):
        csvfile = Path(__file__).parent.parent.parent.joinpath('data', 'data', 'DBData_clean.csv')
        self.df_initial = pd.read_csv(csvfile)
        geojson_file = Path(__file__).parent.parent.parent.joinpath('data', 'data', 'countries.geojson')
        with open(geojson_file) as f:
            self.geojson = json.load(f)

    def df_initialise(self, csv):
        self.df_taxes = csv[csv['Indicator Name'] == 'Paying taxes (DB17-20 methodology) - Score']
        self.df_business = csv[csv['Indicator Name'] == 'Global: Ease of doing business score (DB17-20 methodology)']

    def create_lists(self, df):
        self.years = ['2016', '2017', '2018', '2019', '2020']
        self.countries = list(df['Country Name'])
        self.country_codes = list(df['Country Code'])

    def process_data(self, year, df1, df2):
        self.tax_scores = []
        self.business_scores = []
        df = pd.DataFrame()
        for score in df1[year]:
            self.tax_scores.append(score)
        for score in df2[year]:
            self.business_scores.append(score)
        df = df.assign(country=self.countries, year=year, code=self.country_codes,
                       tax_score=self.tax_scores, business_score=self.business_scores)
        return df

