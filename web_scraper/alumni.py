import pandas as pd
import re
import requests

from bs4 import BeautifulSoup
from web_scraper import CmuScraper
from urllib.request import urlopen, Request
from PyPDF2 import PdfFileReader
from io import BytesIO

from utils.dissertation_pdfs import scrape_dissertation_pages
from utils.abstracts import scrape_dissertation_abstracts


class AlumniPeoplePageScraper(CmuScraper):
    def __init__(self, test=False):
        super().__init__(test=test)
        self.label = 'alumni_phd'
        self.url = self.route_root + 'alumni-phd.html'

    def scrape_site(self):
        if self.soup is None:
            self._get_html_soup()

        phd_alumni_grid = self.soup.find("div", attrs={"class": "grid"})
        phd_alums = phd_alumni_grid.find_all("div")

        alumni_data = []
        for alumni in phd_alums:
            name = alumni.find_all('h2')
            if name:
                try:
                    name = name[1]
                except:
                    name = name[0]
                alumni_row = {'name': name.text.strip(),
                              'entity_type': 'student',
                              'entity_subtype': 'alumni'
                              }
                alumni_data.append(alumni_row)
        self.scraped_data = alumni_data

    def get_output_dataframe(self):
        super().get_output_dataframe()
        return self.output_dataframe


class AlumniPdfThesisScraper(CmuScraper):
    def __init__(self, alumni_df, faculty_df):
        super().__init__()
        self.label = 'dissertation_pdf_matches'
        self.route_root = 'https://www.ml.cmu.edu/research/'
        self.url = self.route_root + 'phd-dissertations.html'
        self.alumni_df = alumni_df
        self.faculty_df = faculty_df
        self.dissertation_pdfs = None
        self.alumni_faculty_matches = None

    def get_dissertation_pdfs(self):
        if self.soup is None:
            self._get_html_soup()

        dissertation_links = []
        for link in self.soup.findAll('a', attrs={'href': re.compile("^http://")}):
            dissertation_links.append(link.get('href'))
        dissertation_links = list(set(dissertation_links))

        dissertation_committee_pages = []
        for link in dissertation_links:
            remoteFile = urlopen(Request(link)).read()
            memoryFile = BytesIO(remoteFile)
            pdfFile = PdfFileReader(memoryFile)

            i = 0
            committee_page = False
            num_pages = len(pdfFile.pages)
            while (not committee_page) and (i <= num_pages - 1):
                page = pdfFile.getPage(i).extractText()
                if 'Committee' in page:
                    committee_page = True
                    page = {'link': link,
                            'text': page,
                            }
                    dissertation_committee_pages.append(page)
                elif i >= num_pages - 1:
                    page = {'link': link,
                            'text': 'ERROR'
                            }
                    dissertation_committee_pages.append(page)

                i = i + 1
        self.dissertation_pdfs = dissertation_committee_pages

    def match_alumni_pdfs(self):
        if self.dissertation_pdfs is None:
            self.get_dissertation_pdfs()
        alumnis = self.alumni_df.name.tolist()
        faculty = self.faculty_df.name.tolist()
        alumni_matches = pd.DataFrame.from_dict(scrape_dissertation_pages(self.dissertation_pdfs, alumnis, faculty))
        alumni_faculty_matches = alumni_matches.explode('alumni_match')
        alumni_faculty_matches = alumni_faculty_matches.explode('faculty_matches')
        alumni_faculty_matches['faculty_matches'] = alumni_faculty_matches['faculty_matches'].apply(
            lambda d: d if isinstance(d, list) else [None, None])
        alumni_faculty_matches['faculty_match'] = alumni_faculty_matches['faculty_matches'].map(lambda x: x[0])
        alumni_faculty_matches['faculty_role'] = alumni_faculty_matches['faculty_matches'].map(lambda x: x[1])
        alumni_faculty_matches = alumni_faculty_matches[['alumni_match', 'faculty_match', 'faculty_role']]
        alumni_faculty_matches = alumni_faculty_matches[
            ~(alumni_faculty_matches.alumni_match.isna()) & ~(alumni_faculty_matches.faculty_match.isna())]
        self.alumni_faculty_matches = alumni_faculty_matches

    def get_output_dataframe(self):
        if self.dissertation_pdfs is None:
            self.get_dissertation_pdfs()
        if self.alumni_faculty_matches is None:
            self.match_alumni_pdfs()
        self.output_dataframe = self.alumni_faculty_matches
        return self.output_dataframe


class AlumniAbstractScraper(CmuScraper):
    def __init__(self, alumni_df, faculty_df):
        super().__init__()
        self.label = 'dissertation_abstracts_matches'
        self.route_root = "http://reports-archive.adm.cs.cmu.edu/anon/"
        self.url = "http://reports-archive.adm.cs.cmu.edu/anon/"
        self.alumni_df = alumni_df
        self.faculty_df = faculty_df
        self.abstracts = None
        self.alumni_faculty_matches = None

    def get_abstracts(self):
        if self.soup is None:
            self._get_html_soup()

        abstracts = []
        year_links = self.soup.select("a[href*=ml20]")
        for year in year_links:
            root = self.url + year.text + '/abstracts/'
            soup = BeautifulSoup(requests.get(root).text, features="html.parser")
            abstract_links = soup.find_all("a", href=re.compile('-.+\.html'))
            abstract_links = list(map(lambda x: BeautifulSoup(requests.get(root + x.text).text, features="html.parser"),
                                      abstract_links
                                      )
                                  )
            abstract_links = list(map(lambda x: {'text': x.text}, abstract_links))
            abstracts = abstracts + abstract_links

        self.abstracts = [x for x in abstracts if x['text'] is not None]

    def match_alumni_abstracts(self):
        if self.abstracts is None:
            self.get_abstracts()
        alumnis = self.alumni_df.name.tolist()
        faculty = self.faculty_df.name.tolist()
        alumni_matches = pd.DataFrame.from_dict(scrape_dissertation_abstracts(self.abstracts, alumnis, faculty))
        alumni_faculty_matches = alumni_matches.explode('alumni_match')
        alumni_faculty_matches = alumni_faculty_matches.explode('faculty_matches')
        alumni_faculty_matches['faculty_matches'] = alumni_faculty_matches['faculty_matches'].apply(
            lambda d: d if isinstance(d, list) else [None, None])
        alumni_faculty_matches['faculty_match'] = alumni_faculty_matches['faculty_matches'].map(lambda x: x[0])
        alumni_faculty_matches['faculty_role'] = alumni_faculty_matches['faculty_matches'].map(lambda x: x[1])
        alumni_faculty_matches = alumni_faculty_matches[['alumni_match', 'faculty_match', 'faculty_role']]
        alumni_faculty_matches = alumni_faculty_matches[
            ~(alumni_faculty_matches.alumni_match.isna()) & ~(alumni_faculty_matches.faculty_match.isna())]
        self.alumni_faculty_matches = alumni_faculty_matches

    def get_output_dataframe(self):
        if self.abstracts is None:
            self.get_abstracts()
        if self.alumni_faculty_matches is None:
            self.match_alumni_abstracts()
        self.output_dataframe = self.alumni_faculty_matches
        return self.output_dataframe
