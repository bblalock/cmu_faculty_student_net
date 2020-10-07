import pandas as pd
from bs4 import BeautifulSoup
import requests
from constants import ROOT_DIR


class CmuScraper:
    def __init__(self, test=False):
        self.test = test
        self.route_root = ROOT_DIR + "/data/raw/" if self.test else "https://www.ml.cmu.edu/people/"
        self.output_dir = ROOT_DIR + "/data/scraped/"
        self.label = None
        self.soup = None
        self.url = None
        self.scraped_data = None
        self.output_dataframe = None

    def _get_html_soup(self):
        if self.test:
            with open(self.url, 'r') as file:
                html_content = file.read()
        else:
            html_content = requests.get(self.url).text
        self.soup = BeautifulSoup(html_content, features="html.parser")

    def scrape_site(self):
        pass

    def get_output_dataframe(self):
        if self.output_dataframe is None:
            self.scrape_site()
        self.output_dataframe = pd.DataFrame(self.scraped_data)

    def write_to_csv(self, loc=None):
        if self.output_dataframe is None:
            self.get_output_dataframe()
        if loc is None:
            loc = self.output_dir + self.label + '.csv'
        self.output_dataframe.to_csv(loc, index=False)
