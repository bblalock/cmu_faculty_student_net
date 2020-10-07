from web_scraper import CmuScraper
import re


class RelatedFacultyScraper(CmuScraper):
    def __init__(self, test=False):
        super().__init__(test=test)
        self.label = 'related_faculty'
        self.url = self.route_root + 'related-faculty.html'

    def scrape_site(self):
        if self.soup is None:
            self._get_html_soup()

        mld_affiliated_fac = self.soup.find_all("div", attrs={'class': 'content'})

        related_faculty_data = []
        for faculty in mld_affiliated_fac:
            name = faculty.find('h2')
            if name:
                faculty_row = {'entity_type': 'faculty', 'faculty_type': 'related',
                               'name': re.sub("\s+", ' ', name.text.strip().replace('\n', ''))
                               }

                title = faculty.find('h3')
                faculty_row['title'] = title.text.strip().replace('\n', '')

                related_faculty_data.append(faculty_row)
        self.scraped_data = related_faculty_data

    def get_output_dataframe(self):
        super().get_output_dataframe()
        return self.output_dataframe
